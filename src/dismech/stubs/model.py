"""Loading, slugging, and checking of curation stubs under `stubs/`."""

from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from dismech.compare.mondo_priority import iter_covered_mondo_ids
from dismech.yaml_io import safe_load

MONDO_ID_PATTERN = re.compile(r"^MONDO:[0-9]{7}$")

#: MONDO marks retired concepts by prefixing the label. Such a term is not a
#: curation target under any reading, so a stub for one is an error rather than
#: a judgement call. Same backstop the prioritizer config carries, for candidate
#: exports that do not populate `is_obsolete`.
OBSOLETE_LABEL_PATTERN = re.compile(r"^\s*obsolete\b", re.IGNORECASE)

#: A label or synonym has to carry some information before a collision with a KB
#: entry means anything. An acronym -- `AIP`, `Bss`, `CRD` -- collides by
#: coincidence, so short or single-word strings are not compared.
_MIN_INFORMATIVE_CHARS = 8
_MIN_INFORMATIVE_WORDS = 2
_NORMALIZE_STRIP = re.compile(r"[^a-z0-9 ]+")

#: Statuses a stub may carry. Mirrors StubStatusEnum in the schema. There is no
#: CLAIMED: claims live on GitHub as `claim`-labelled issues, because a claim
#: written into YAML only becomes visible when its PR merges. See claims.py.
STATUSES = ("OPEN", "BLOCKED", "DEFERRED")
#: Entry-type decisions. Mirrors StubEntryTypeEnum in the schema.
ENTRY_TYPES = ("UNDECIDED", "DISEASE", "GROUPING", "SUBTYPE", "OUT_OF_SCOPE")
#: Priority bands. Mirrors StubPriorityEnum in the schema.
PRIORITIES = ("HIGH", "NORMAL", "LOW")

_PRIORITY_ORDER = {"HIGH": 0, "NORMAL": 1, "LOW": 2}

# Characters that survive into a filename stem. `kb/disorders/` uses
# Title_Case_With_Underscores and tolerates digits, hyphens, and periods
# (`22q11.2_Deletion_Syndrome.yaml`), so the stub slug uses the same alphabet.
_SLUG_KEEP = re.compile(r"[^A-Za-z0-9.\- ]+")
_SLUG_SPACE = re.compile(r"\s+")


def normalize_label(value: Any) -> str:
    """Casefold and strip punctuation so labels compare across styles.

    `Wilms' tumor` and `Wilms tumor`, `Desanto-Shinawi` and `DeSanto-Shinawi`.
    """
    if not value:
        return ""
    folded = unicodedata.normalize("NFKD", str(value))
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    folded = _NORMALIZE_STRIP.sub(" ", folded.lower())
    return re.sub(r"\s+", " ", folded).strip()


def is_informative_label(normalized: str) -> bool:
    """Whether a normalized label is specific enough to match on."""
    return (
        len(normalized) >= _MIN_INFORMATIVE_CHARS
        and len(normalized.split()) >= _MIN_INFORMATIVE_WORDS
    )


def entry_label_strings(data: dict[str, Any]) -> list[str]:
    """Every name a KB entry answers to: name, display name, term label, synonyms."""
    disease_term = data.get("disease_term") or {}
    labels: list[Any] = [
        data.get("name"),
        data.get("display_name"),
        (disease_term.get("term") or {}).get("label"),
        disease_term.get("preferred_term"),
    ]
    for synonym in data.get("synonyms") or []:
        labels.append(
            synonym if isinstance(synonym, str) else (synonym or {}).get("name")
        )
    return [str(label) for label in labels if label]


def default_repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def default_stub_dir() -> Path:
    return default_repo_root() / "stubs"


def default_kb_dirs() -> list[Path]:
    root = default_repo_root()
    return [root / "kb" / "disorders", root / "kb" / "groupings"]


def slugify_label(label: str) -> str:
    """Turn a MONDO label into a `kb/disorders`-style filename stem.

    `alcohol sensitivity, acute` -> `Alcohol_Sensitivity_Acute`. Accents are
    folded rather than dropped so `Behçet` becomes `Behcet`, not `Behet`.

    Deliberately **not** `dismech.export.utils.slugify`, in the same way
    `hpoa_export.slugify` is not. That one turns an entry `name` -- already
    written in the repository's Title_Case style -- into a page filename, and
    must stay byte-identical across the renderer and every exporter or the
    browser index dead-links. This one turns an *ontology label*, which is
    lowercase and carries commas and accents, into a proposed entry name. They
    take different inputs and answer different questions; sharing them would
    couple the page build to MONDO's labelling conventions.
    """
    folded = unicodedata.normalize("NFKD", label)
    folded = "".join(ch for ch in folded if not unicodedata.combining(ch))
    cleaned = _SLUG_KEEP.sub(" ", folded)
    cleaned = _SLUG_SPACE.sub(" ", cleaned).strip()
    if not cleaned:
        return ""
    words = []
    for word in cleaned.split(" "):
        # Leave words that already carry internal capitals or digits alone
        # (`22q11.2`, `IgG4`, `BRAF`); title-case the rest.
        words.append(
            word if any(c.isupper() or c.isdigit() for c in word) else word.capitalize()
        )
    return "_".join(words)


def stub_filename(label: str, mondo_id: str) -> str:
    """Filename for a stub. Falls back to the MONDO ID when the label won't slug."""
    slug = slugify_label(label)
    if not slug:
        return f"{mondo_id.replace(':', '_')}.yaml"
    return f"{slug}.yaml"


@dataclass
class Stub:
    """One stub file, as loaded from disk."""

    path: Path
    data: dict[str, Any]

    @property
    def mondo_id(self) -> str:
        return str(self.data.get("mondo_id") or "")

    @property
    def label(self) -> str:
        return str(self.data.get("label") or "")

    @property
    def status(self) -> str:
        return str(self.data.get("status") or "OPEN")

    @property
    def entry_type(self) -> str:
        return str(self.data.get("entry_type") or "UNDECIDED")

    @property
    def priority(self) -> str:
        return str(self.data.get("priority") or "NORMAL")

    @property
    def sort_key(self) -> tuple[int, str]:
        """Priority band, then a stable hash of the MONDO ID.

        Deliberately not alphabetical. Alphabetical order clusters the queue by
        naming convention -- five `10q..` microdeletion syndromes in a row --
        which makes the head of the list look like a recommendation for a
        family of diseases when it is an artifact of sorting. Hashing gives a
        spread that is arbitrary (as it should be, since priority within a band
        is genuinely unranked) but reproducible across runs and machines.
        """
        digest = hashlib.sha256(self.mondo_id.encode("utf-8")).hexdigest()
        return (_PRIORITY_ORDER.get(self.priority, 1), digest)

    @property
    def alpha_sort_key(self) -> tuple[int, str]:
        return (_PRIORITY_ORDER.get(self.priority, 1), self.label.casefold())


@dataclass
class StubIssue:
    """A problem found by :func:`check_stubs`.

    `severity` separates a malformed file from a stale one, and only the first
    gates.

    An `error` means the file itself is broken — unparseable, a malformed MONDO
    ID, a duplicate of another stub, a bad enum value. Only the person who wrote
    that stub sees it, and it is cheap for them to fix.

    An `advisory` means the queue has drifted: the disease got curated by
    somebody else, the MONDO term was retired, a similarly named entry already
    exists. **These must never gate.** Stubs are informative, not curated
    content — a curation PR merging on `main` would otherwise turn every open
    stub PR red through no fault of its author, and curators would spend their
    time servicing a bookkeeping message. Overlap and lag are expected; a
    periodic tidy-up pass (`dismech-stubs tidy`) clears them.
    """

    path: Path | None
    kind: str
    message: str
    severity: str = "error"

    def format(self) -> str:
        where = self.path.name if self.path else "stubs/"
        prefix = "" if self.severity == "error" else f"[{self.severity}] "
        return f"{prefix}{where}: {self.kind}: {self.message}"


@dataclass
class CoverageIndex:
    """MONDO IDs already accounted for by a committed KB entry."""

    ids: dict[str, str] = field(default_factory=dict)
    #: Normalized label/synonym -> "disorders/Foo.yaml". Catches a disease the KB
    #: curated under a *different* MONDO ID, which the ID index cannot see.
    labels: dict[str, str] = field(default_factory=dict)

    def covered_by(self, mondo_id: str) -> str | None:
        return self.ids.get(mondo_id)

    def entry_labelled(self, label: str) -> str | None:
        normalized = normalize_label(label)
        if not is_informative_label(normalized):
            return None
        return self.labels.get(normalized)


def _grouping_mondo_ids(data: dict[str, Any]) -> list[str]:
    """MONDO IDs a `kb/groupings/` entry claims.

    Groupings have no `disease_term`; they carry the concept in
    `mappings.mondo_mappings`. `mondo_priority.build_coverage_index` never reads
    this directory, which is why concepts already modelled as groupings kept
    reappearing in the priority queue (dismech#8768).

    Every mapping predicate counts here, unlike `iter_covered_mondo_ids`, which
    honours only exact/narrow. The predicates say different things in the two
    places. On a disease entry a broad/close/related mapping is a cross-reference
    to some *other* concept, so it must not retire that concept. On a grouping it
    records how the grouping sits against the MONDO term it was built around --
    and every one of them in the KB today names a grouping-level concept
    (`ciliopathy`, `RASopathy`, `inborn errors of metabolism`, `microcephaly`),
    which is precisely what should not be sitting in a disorder curation queue.

    This retires the concept from the queue; it does not assert it has been
    curated as a disease. The check message names the grouping file, so a curator
    who disagrees can see what made the call.
    """
    out = []
    for mapping in (data.get("mappings") or {}).get("mondo_mappings") or []:
        if not isinstance(mapping, dict):
            continue
        term_id = (mapping.get("term") or {}).get("id")
        if term_id:
            out.append(str(term_id))
    return out


def build_coverage_index(kb_dirs: list[Path] | None = None) -> CoverageIndex:
    """Index every MONDO ID a committed KB entry already covers.

    Reads `kb/disorders/` (root `disease_term`, `has_subtypes[].subtype_term`,
    and exact/narrow `mondo_mappings`) *and* `kb/groupings/` — a stub whose
    concept is already a grouping is finished work, not an open gap.
    """
    index = CoverageIndex()
    for kb_dir in kb_dirs or default_kb_dirs():
        if not kb_dir.is_dir():
            continue
        is_grouping = kb_dir.name == "groupings"
        for path in sorted(kb_dir.glob("*.yaml")):
            if path.name.endswith(".history.yaml"):
                continue
            data = safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                continue
            rel = f"{kb_dir.name}/{path.name}"
            for label in entry_label_strings(data):
                normalized = normalize_label(label)
                if is_informative_label(normalized):
                    index.labels.setdefault(normalized, rel)
            if is_grouping:
                for mondo_id in _grouping_mondo_ids(data):
                    index.ids.setdefault(mondo_id, rel)
            else:
                for mondo_id, _ in iter_covered_mondo_ids(data, path.name):
                    index.ids.setdefault(mondo_id, rel)
    return index


def iter_stub_files(stub_dir: Path | None = None) -> list[Path]:
    directory = stub_dir or default_stub_dir()
    if not directory.is_dir():
        return []
    return sorted(directory.glob("*.yaml"))


def load_stub(path: Path) -> Stub:
    data = safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Stub at {path} must be a YAML object")
    return Stub(path=path, data=data)


def load_stubs(stub_dir: Path | None = None) -> list[Stub]:
    return [load_stub(path) for path in iter_stub_files(stub_dir)]


def load_stubs_reporting_errors(
    stub_dir: Path | None = None,
) -> tuple[list[Stub], list[StubIssue]]:
    """Load every stub, turning a parse failure into a finding rather than a raise.

    Anyone can add a stub by pull request, so a malformed one is a normal thing
    to encounter. Letting it propagate meant a single bad file aborted the whole
    check with a traceback and said nothing about the other 1,866 -- the least
    useful moment to lose the report.
    """
    stubs: list[Stub] = []
    issues: list[StubIssue] = []
    for path in iter_stub_files(stub_dir):
        try:
            stubs.append(load_stub(path))
        except Exception as exc:
            # YAML parse errors are multi-line; flattened so the report stays
            # one finding per line, with the filename in front of it.
            detail = " ".join(str(exc).split())
            issues.append(
                StubIssue(path, "unparseable", f"{type(exc).__name__}: {detail}")
            )
    return stubs, issues


def check_stubs(
    stub_dir: Path | None = None,
    kb_dirs: list[Path] | None = None,
    coverage: CoverageIndex | None = None,
) -> list[StubIssue]:
    """Check every stub, returning findings of both severities.

    Only `error` findings mean something is wrong: the *file* is broken —
    unparseable, a malformed MONDO ID, a duplicate of another stub, a bad enum
    value. Only the author of that stub sees those, and they are cheap to fix.

    `advisory` findings mean the *queue* drifted — the disease got curated by
    somebody else, MONDO retired the term, a similarly named entry exists under
    a different ID. **These never gate.** Stubs are informative, not curated
    content; gating on drift would make every open stub PR hostage to unrelated
    curation merges. `dismech-stubs tidy` sweeps them instead.

    A single stub can produce more than one advisory, so callers acting on these
    (deleting files, counting stubs) must deduplicate by path.
    """
    stubs, issues = load_stubs_reporting_errors(stub_dir)
    index = coverage if coverage is not None else build_coverage_index(kb_dirs)

    seen_ids: dict[str, Path] = {}
    for stub in stubs:
        path = stub.path
        mondo_id = stub.mondo_id

        if not mondo_id:
            issues.append(StubIssue(path, "missing_mondo_id", "no `mondo_id`"))
            continue
        if not MONDO_ID_PATTERN.match(mondo_id):
            issues.append(
                StubIssue(path, "bad_mondo_id", f"{mondo_id!r} is not MONDO:NNNNNNN")
            )
        if not stub.label:
            issues.append(StubIssue(path, "missing_label", "no `label`"))
        elif OBSOLETE_LABEL_PATTERN.match(stub.label):
            issues.append(
                StubIssue(
                    path,
                    "obsolete_term",
                    f"{mondo_id} is an obsolete MONDO term — stale, tidy up",
                    severity="advisory",
                )
            )

        if stub.status not in STATUSES:
            issues.append(
                StubIssue(path, "bad_status", f"{stub.status!r} not in {STATUSES}")
            )
        if stub.entry_type not in ENTRY_TYPES:
            issues.append(
                StubIssue(
                    path, "bad_entry_type", f"{stub.entry_type!r} not in {ENTRY_TYPES}"
                )
            )
        if stub.priority not in PRIORITIES:
            issues.append(
                StubIssue(
                    path, "bad_priority", f"{stub.priority!r} not in {PRIORITIES}"
                )
            )

        previous = seen_ids.get(mondo_id)
        if previous is not None:
            issues.append(
                StubIssue(
                    path,
                    "duplicate_mondo_id",
                    f"{mondo_id} also claimed by {previous.name}",
                )
            )
        else:
            seen_ids[mondo_id] = path

        expected = stub_filename(stub.label, mondo_id)
        # Two MONDO concepts can slug identically, in which case the seeder
        # disambiguates with the ID. Both spellings are legal.
        disambiguated = (
            f"{slugify_label(stub.label)}__{mondo_id.replace(':', '_')}.yaml"
        )
        if stub.label and path.name not in {expected, disambiguated}:
            issues.append(StubIssue(path, "filename_mismatch", f"expected {expected}"))

        covered_by = index.covered_by(mondo_id)
        if covered_by:
            issues.append(
                StubIssue(
                    path,
                    "already_curated",
                    f"{mondo_id} is covered by {covered_by} — stale, tidy up",
                    severity="advisory",
                )
            )
            continue

        # Same name, different MONDO ID. The ID index cannot see this, and the
        # answer genuinely varies: `Friedreich ataxia 1` (MONDO:0100340) against
        # a curated `Friedreich_Ataxia` may want deleting or may want a mapping
        # added to the existing entry, while `Leber congenital amaurosis type 1`
        # against a gene-first `GUCY2D-Related_Retinopathy` is arguably a
        # distinct entry. A person has to decide, so this is advisory.
        candidates = [stub.label, *(stub.data.get("synonyms") or [])]
        for candidate in candidates:
            same_disease = index.entry_labelled(candidate)
            if not same_disease:
                continue
            via = (
                ""
                if normalize_label(candidate) == normalize_label(stub.label)
                else (f" (via synonym {candidate!r})")
            )
            issues.append(
                StubIssue(
                    path,
                    "possible_kb_duplicate",
                    f"{same_disease} answers to this name{via} "
                    "but curates a different MONDO ID",
                    severity="advisory",
                )
            )
            break

    return issues
