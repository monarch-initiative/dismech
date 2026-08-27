"""Tests for the phenotype-profile schema and tooling.

Covers three things: that the schema and its worked example stay valid, that
the lint catches the inconsistencies the schema itself cannot express, and that
the reference-cache export keeps the contract curator-quoted snippets depend on.
"""

from __future__ import annotations

import copy
from pathlib import Path

import pytest
from linkml_runtime.utils.schemaview import SchemaView

from dismech.phenotype_distribution import (
    Collection,
    discover_collections,
    lint_collections,
    load_collection,
    profile_cache_entry,
    render_profile_body,
    write_cache_files,
)
from dismech.reference_cache_frontmatter import main as frontmatter_main

REPO_ROOT = Path(__file__).resolve().parents[1]

SCHEMA_PATH = REPO_ROOT / "src" / "dismech" / "schema" / "phenotype_distribution.yaml"
NATIVE_SCHEMA_PATH = REPO_ROOT / "src" / "dismech" / "schema" / "dismech.yaml"
#: Prose that repeats a list the code also enforces. Kept repo-relative because
#: `git show HEAD:<path>` resolves from the repo root; join onto REPO_ROOT for a
#: working-tree read, so the guards survive pytest being invoked from elsewhere.
CLAUDE_MD_PATH = Path("CLAUDE.md")
DOCS_PATH = Path("docs/phenotype-distributions.md")
EXAMPLES_DIR = REPO_ROOT / "examples" / "phenotype_distributions"
KB_DIR = REPO_ROOT / "kb" / "phenotype_distributions"

TARGET_CLASS = "ProfileSet"


def _example_paths() -> list[Path]:
    return sorted(EXAMPLES_DIR.glob("*.yaml"))


def _all_paths() -> list[Path]:
    return sorted(EXAMPLES_DIR.glob("*.yaml")) + sorted(KB_DIR.glob("*.yaml"))


def _renderable_collections():
    """Collections the cache renderer will accept (everything not illustrative)."""
    return [
        c
        for c in discover_collections(_all_paths())
        if c.data.get("provenance_tier") != "ILLUSTRATIVE"
    ]


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------


def test_evidence_direction_values_match_native_dismech_support_enum() -> None:
    """SEPIO direction must stay inter-convertible with native `supports`.

    The whole point of copying the vocabulary is that a native evidence item
    and a SEPIO evidence line say "SUPPORT" the same way; a drift here would
    silently break that.
    """
    sv = SchemaView(str(SCHEMA_PATH))
    native = SchemaView(str(NATIVE_SCHEMA_PATH))
    ours = set(sv.get_enum("EvidenceDirectionEnum").permissible_values)
    theirs = set(native.get_enum("EvidenceItemSupportEnum").permissible_values)
    assert ours == theirs


def test_profile_method_values_stay_a_subset_of_the_native_association_enum() -> None:
    """Pin the claim `ProfileMethodEnum`'s own description makes.

    That description says every value here is also a value of the native
    `AssociationSignalMethodEnum`. Unguarded, that is prose, and prose about
    this schema has rotted five times already — adding one value falsifies the
    sentence and nothing notices.

    I first declined this guard, on the argument that pinning the enum would
    assert it should exist, when deleting it in favour of the native one is the
    open proposal. That was wrong: the guard is conditional. It says *if* this
    enum exists it stays a subset, which holds under every restructuring option
    — and under the one that reuses the native enum, this test is deleted along
    with the thing it guards. Nothing here argues for keeping it.

    Deliberately subset rather than set-equality, unlike the
    `EvidenceDirectionEnum` guard above: the native enum has two values
    (`EHR_TEMPORAL_COMORBIDITY`, `LITERATURE_ASSOCIATION`) that describe no way
    a profile is derived, so equality would be the wrong claim.
    """
    sv = SchemaView(str(SCHEMA_PATH))
    native = SchemaView(str(NATIVE_SCHEMA_PATH))
    ours = set(sv.get_enum("ProfileMethodEnum").permissible_values)
    theirs = set(native.get_enum("AssociationSignalMethodEnum").permissible_values)
    assert ours <= theirs, (
        "ProfileMethodEnum has values the native AssociationSignalMethodEnum "
        f"does not: {sorted(ours - theirs)}. Either add them there too, or "
        "amend the enum description, which claims this cannot happen."
    )


@pytest.mark.parametrize("path", _all_paths(), ids=lambda p: p.name)
def test_collections_validate_against_schema(path: Path) -> None:
    from linkml.validator import validate_file

    report = validate_file(str(path), str(SCHEMA_PATH), TARGET_CLASS)
    assert not report.results, [r.message for r in report.results]


# ---------------------------------------------------------------------------
# Lint
# ---------------------------------------------------------------------------


def test_examples_lint_clean() -> None:
    result = lint_collections(discover_collections(_all_paths()))
    assert result.errors == [], [i.format() for i in result.errors]
    assert result.warnings == [], [i.format() for i in result.warnings]
    assert result.n_profiles > 0


def _mutate(path: Path, mutator) -> Collection:
    coll = load_collection(path)
    coll = Collection(path=coll.path, data=copy.deepcopy(coll.data))
    mutator(coll.data)
    return coll


def _error_messages(coll: Collection) -> str:
    return " ".join(i.message for i in lint_collections([coll]).errors)


# ---------------------------------------------------------------------------
# Reference-cache export
# ---------------------------------------------------------------------------


def test_illustrative_collections_cannot_be_rendered_into_the_cache(
    tmp_path: Path,
) -> None:
    """Synthetic numbers must not be able to become citable, even by mistake.

    Built by re-tiering a real set rather than read from a file: the tier guard
    has to hold for whatever someone writes next, not only for a committed
    example that happens to carry the tier today.
    """

    def mutate(data):
        data["provenance_tier"] = "ILLUSTRATIVE"

    illustrative = [_mutate(EXAMPLES_DIR / "charmpheno_population_eds.yaml", mutate)]
    with pytest.raises(ValueError, match="ILLUSTRATIVE"):
        write_cache_files(illustrative, tmp_path)
    assert not list(tmp_path.glob("*.md"))


def test_write_cache_files_prunes_orphaned_profiles(tmp_path: Path) -> None:
    """A renamed or deleted profile must not leave a citable cache file behind."""
    collections = _renderable_collections()
    write_cache_files(collections, tmp_path)
    orphan = tmp_path / "PHENODIST_GONE-FOREVER-001.md"
    orphan.write_text("---\nreference_id: x\n---\n", encoding="utf-8")
    _written, pruned = write_cache_files(collections, tmp_path)
    assert orphan.name in {p.name for p in pruned}
    assert not orphan.exists()


def test_clinical_trial_quotes_resolve_to_the_right_cache_file() -> None:
    """Trials are cited `clinicaltrials:NCT…` and cached `clinicaltrials_NCT….md`.

    A bare `NCT` prefix failed both ways: it silently skipped the real citation
    form, and it manufactured a never-existing `NCT….md` path for the other.
    """
    from dismech.phenotype_distribution import _cache_path_for

    cache = REPO_ROOT / "references_cache"
    assert _cache_path_for("clinicaltrials:NCT00000146", cache) == (
        cache / "clinicaltrials_NCT00000146.md"
    )
    # And that file really is the naming convention used in this repo.
    assert (cache / "clinicaltrials_NCT00000146.md").exists()
    assert not list(cache.glob("NCT[0-9]*.md"))


def _verifiable_prefix_bullet() -> str:
    """The docs bullet listing which document prefixes get quote-verified.

    Bounded to the bullet itself — a fixed character window trails into the
    following bullet, where an unrelated mention would satisfy the check.
    """
    docs = (REPO_ROOT / DOCS_PATH).read_text(encoding="utf-8")
    lines = docs.splitlines()
    starts = [i for i, ln in enumerate(lines) if "citing a fetchable document" in ln]
    assert starts, (
        "the docs sentence this test pins no longer exists; if it was reworded, "
        "update this test rather than deleting it"
    )
    start = starts[0]
    end = start + 1
    while end < len(lines) and not (
        lines[end].lstrip().startswith("- **") or lines[end].startswith("#")
    ):
        end += 1
    return "\n".join(lines[start:end])


def _warning_messages(coll: Collection) -> str:
    return " ".join(i.message for i in lint_collections([coll]).warnings)


def test_docs_prefix_list_matches_the_code_exactly() -> None:
    """Pin the docs to the code, in both directions.

    This sentence has been wrong twice: first naming a bare `NCT` that is not a
    cache convention at all (which produced the original bug), then reading as
    exhaustive while omitting `PHENODIST:`. Fixing prose a third time without a
    guard just sets up a fourth.

    Both directions matter, and the second one more. Docs omitting a prefix
    under-promises, which is merely untidy. Docs listing a prefix the code does
    not verify *over*-promises: a curator reads it, believes their quote was
    checked, and it never was — the same failure the LOINC caveat exists to
    prevent.
    """
    import re

    from dismech.phenotype_distribution import _VERIFIABLE_PREFIXES

    bullet = _verifiable_prefix_bullet()
    # Digits and hyphens are in the class because this repo already uses
    # prefixes that need them (`ICD10CM:`, `icd11f:` in conf/oak_config.yaml).
    # A narrower class would silently fail to extract such a prefix from the
    # docs and report it as undocumented when it is documented — a false alarm
    # whose cause would be hard to see from the assertion message.
    documented = set(re.findall(r"`([A-Za-z0-9_-]+:)`", bullet))
    coded = set(_VERIFIABLE_PREFIXES)

    assert not (coded - documented), (
        f"docs omit verified prefixes: {sorted(coded - documented)}"
    )
    assert not (documented - coded), (
        "docs claim verification for prefixes the code does not check: "
        f"{sorted(documented - coded)}"
    )


def _committed_text(path: Path) -> str | None:
    """`path` as of HEAD, or None outside a git checkout.

    Deliberately does not fall back to the working tree on failure: the point of
    reading the committed blob is to be unaffected by local mutation, and a
    silent fallback would reintroduce exactly what it exists to avoid.
    """
    import subprocess

    try:
        out = subprocess.run(
            ["git", "show", f"HEAD:{path.as_posix()}"],
            capture_output=True,
            check=True,
            cwd=REPO_ROOT,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return out.stdout.decode("utf-8")


def test_a_yaml_that_is_not_a_collection_is_rejected(tmp_path: Path) -> None:
    """Silently treating the wrong file as an empty collection is worse than failing.

    The failure mode is a clean bill of health for a run that checked nothing:
    point the lint at the schema by mistake and it reports a record count and no
    findings, which reads exactly like success.
    """
    not_a_collection = tmp_path / "wrong.yaml"
    not_a_collection.write_text(
        "id: https://example.org/x\nname: x\n", encoding="utf-8"
    )
    with pytest.raises(ValueError, match="not a phenotype profile set"):
        load_collection(not_a_collection)

    # The real schema is the file most likely to be passed by mistake.
    with pytest.raises(ValueError, match="not a phenotype profile set"):
        load_collection(SCHEMA_PATH)

    # And a genuine profile set still loads.
    assert load_collection(EXAMPLES_DIR / "charmpheno_population_eds.yaml").data


def test_cli_reports_bad_paths_as_errors_not_tracebacks(capsys) -> None:
    """A mistyped path is the likeliest user error, so it must read like one.

    The CLI already decided this shape for the provenance-tier guard. A
    traceback for the far more common mistake would be the inconsistency.
    """
    from dismech.phenotype_distribution import main

    for bad in (str(SCHEMA_PATH), str(EXAMPLES_DIR / "does-not-exist.yaml")):
        assert main([bad]) == 1
        out = capsys.readouterr().out
        assert out.startswith("[ERROR] "), out
        assert bad in out


def test_single_collection_rebuild_does_not_prune_other_collections() -> None:
    """Naming one collection file must not delete every other cache file."""
    from dismech.phenotype_distribution import _is_full_rebuild

    assert _is_full_rebuild(None) is True
    assert _is_full_rebuild([]) is True
    assert _is_full_rebuild([Path("kb/phenotype_distributions")]) is True
    assert _is_full_rebuild([Path("kb/phenotype_distributions/one.yaml")]) is False


def test_discover_collections_tolerates_a_missing_directory() -> None:
    """A collection set that does not exist yet is not an error."""
    assert discover_collections([Path("kb/phenotype_distributions")]) == []
    with pytest.raises(FileNotFoundError):
        discover_collections([Path("kb/phenotype_distributions/nope.yaml")])


def _quoted_item(data: dict) -> dict:
    """The one evidence item in the example that cites a fetchable document.

    The example's own item cites a GitHub URL, which is deliberately not a
    verifiable prefix, so the two tests below first repoint it at a PMID that is
    cached for an unrelated kb entry — and therefore stays cached — before
    breaking it. Found by walking rather than by a fixed index, so adding an
    evidence line to the example does not silently move the target.
    """
    for profile in data["profiles"]:
        for line in profile.get("evidence_lines") or []:
            for item in line.get("has_evidence_items") or []:
                return item
    raise AssertionError("the example carries no evidence item to check")


def test_lint_rejects_a_quote_not_in_the_cited_reference(
    profile_set_path: Path,
) -> None:
    """Blocks laundering an unverified quote through the PHENODIST cache."""

    def mutate(data):
        item = _quoted_item(data)
        item["reported_in"]["id"] = "PMID:30986316"
        item["item_value"] = "This sentence is not in the paper."

    assert "not a verbatim substring" in _error_messages(
        _mutate(profile_set_path, mutate)
    )


def test_lint_rejects_a_quote_whose_reference_is_not_cached(
    profile_set_path: Path,
) -> None:
    def mutate(data):
        _quoted_item(data)["reported_in"]["id"] = "PMID:99999999"

    assert "is not cached" in _error_messages(_mutate(profile_set_path, mutate))


def test_float_rendering_does_not_truncate_precision() -> None:
    """The quotable row must not silently round a tight parameter."""
    from dismech.phenotype_distribution import _fmt

    assert _fmt(5.272386501517754) == "5.272386501517754"
    assert _fmt(1.5071340388291068e-38) == "1.5071340388291068e-38"
    assert _fmt(1070.0) == "1070"


def _unperformed_lookups(issues) -> list[str]:
    """Warnings meaning the lookup did not happen, rather than that it failed.

    `check_terms` reports an unreachable adapter and an errored lookup as
    WARNINGs, deliberately: not being able to check a term is not evidence the
    term is wrong. A test asserting on the *result* of a lookup has to make the
    same distinction, or it reports a flaky network as a code defect.

    Matches the module's own constants rather than literal text. `Issue` has no
    structural kind field, so this is still substring matching — but against a
    name the emitting code shares, and
    `test_unperformed_lookup_phrases_match_what_the_code_emits` pins that the
    real messages still contain them. Hard-coded literals would let a reword
    silently return this file to being intermittently red, which is the exact
    symptom the skip exists to fix.
    """
    from dismech.phenotype_distribution import (
        UNPERFORMED_ADAPTER,
        UNPERFORMED_RESOLVE,
    )

    return [
        i.message
        for i in issues
        if i.severity == "WARNING"
        and (UNPERFORMED_RESOLVE in i.message or UNPERFORMED_ADAPTER in i.message)
    ]


def test_unperformed_lookup_phrases_match_what_the_code_emits(
    profile_set_path: Path, monkeypatch
) -> None:
    """The skip predicate must recognise the messages actually produced.

    Without this, rewording either warning in `check_terms` makes
    `_unperformed_lookups` silently return nothing, and the wrong-CURIE test
    below stops skipping and goes back to failing whenever OLS is slow — a
    quiet regression to the defect just fixed. Constants make the coupling
    visible; this makes breaking it loud.

    Both branches are exercised against real emissions rather than asserted
    against string literals, so the phrases cannot drift from their use.
    """
    import oaklib

    from dismech.phenotype_distribution import check_terms

    def mutate(data):
        data["disease"]["disease_term"]["term_id"] = "HP:0410017"

    coll = _mutate(profile_set_path, mutate)

    class _RaisingAdapter:
        def label(self, curie: str) -> str | None:
            raise ConnectionError("simulated outage")

    monkeypatch.setattr(oaklib, "get_adapter", lambda spec: _RaisingAdapter())
    assert _unperformed_lookups(check_terms([coll])), (
        "a lookup that raised was not recognised as unperformed; "
        "`UNPERFORMED_RESOLVE` no longer matches what `check_terms` emits"
    )

    def _unloadable(spec):
        raise RuntimeError("simulated adapter load failure")

    monkeypatch.setattr(oaklib, "get_adapter", _unloadable)
    assert _unperformed_lookups(check_terms([coll])), (
        "an adapter that failed to load was not recognised as unperformed; "
        "`UNPERFORMED_ADAPTER` no longer matches what `check_terms` emits"
    )


def test_term_check_reports_a_wrong_label_without_a_local_ontology(
    profile_set_path: Path, monkeypatch
) -> None:
    """The regression guard for the round-1 CURIE, on a runner with no databases.

    The version below needs `hp.db`, nothing in CI provisions it, and a pytest
    skip is indistinguishable from a pass in the checks UI — so the one guard
    against a recurrence of this PR's only red finding was green-by-skip on the
    gate. That is exactly the failure the arithmetic guard was rewritten to
    avoid, one layer up: silence reading as success.

    Splitting it fixes that without a multi-hundred-megabyte download in every
    CI run. Two separate claims were tangled together:

    * *the code reports a label mismatch* — the part that can regress, pinned
      here against a stub adapter, so it runs everywhere;
    * *HP:0410017 really is "Otitis externa"* — an ontology fact, which needs
      real OAK and is still gated below.

    The clean and nonexistent cases are asserted too. A checker that flags
    everything would satisfy the mismatch assertion on its own.
    """
    import oaklib

    from dismech.phenotype_distribution import check_terms, iter_terms

    # Derived from the examples rather than hardcoded. A closed map would make
    # the clean-file assertion below fail the moment anyone adds a term to an
    # example — reporting `does not exist` and blaming the new term, when the
    # term is fine and the fixture simply has not heard of it. The stub is
    # meant to stand in for the ontology, not to pin the example's contents.
    labels = {
        t["term_id"]: t["term_label"]
        for coll in discover_collections(_example_paths())
        for t, _where in iter_terms(coll.data)
    }
    assert labels, "expected the example to declare at least one ontology term"
    # The one deliberate contradiction: the real label of the CURIE that
    # slipped through review, against the disease label the file carries.
    labels["HP:0410017"] = "Otitis externa"

    consulted: list[str] = []

    class _StubAdapter:
        def label(self, curie: str) -> str | None:
            consulted.append(curie)
            return labels.get(curie)

    monkeypatch.setattr(oaklib, "get_adapter", lambda spec: _StubAdapter())

    def wrong_curie(data):
        data["disease"]["disease_term"]["term_id"] = "HP:0410017"

    issues = check_terms([_mutate(profile_set_path, wrong_curie)])
    assert any("Otitis externa" in i.message for i in issues), (
        "term check failed to flag a CURIE whose label is not its own"
    )
    # The patch reaches `check_terms` only because its `get_adapter` import is
    # inside the function. Hoist that import to module scope and the name binds
    # at import time, the stub is bypassed, and this test quietly goes back to
    # consulting real OAK — passing where `hp.db` happens to exist and failing
    # elsewhere for a reason unrelated to its name. A comment would document
    # that coupling; this asserts it.
    assert consulted, (
        "the stub adapter was never consulted, so this test is exercising real "
        "OAK rather than the code path it claims to pin — check that "
        "`check_terms` still imports `get_adapter` inside the function"
    )

    def nonexistent(data):
        data["disease"]["disease_term"]["term_id"] = "HP:9999999"

    assert any(
        "does not exist" in i.message
        for i in check_terms([_mutate(profile_set_path, nonexistent)])
    )

    # And the unmutated file is clean, so the above is not flagging everything.
    #
    # This proves that and nothing more. Since the stub's labels are derived
    # from the same files being checked, it cannot report a label mismatch here
    # by construction — deriving the map bought self-maintenance at the cost of
    # this line meaning anything about whether the example's terms are right.
    # That coverage lives in `test_example_terms_are_all_valid`, which resolves
    # them against real OLS and is deliberately ungated. The two are not
    # redundant; do not delete that one on the strength of this.
    assert not check_terms(discover_collections(_example_paths()))


def test_term_check_catches_a_wrong_curie(profile_set_path: Path) -> None:
    """The same guard against the real ontology, rather than a stub.

    This one pins the *fact* — that HP:0410017 is "Otitis externa" and not the
    disease label it was carrying — which no stub can establish. The code path
    it shares with the test above is covered there unconditionally.

    Aimed at the set-level `disease_term`, which is also the regression guard
    for the walk: lifting `disease` out of the profiles moved the one term
    every set carries outside the loop that used to check terms, so a check
    that only walked profiles would pass this file having verified nothing.

    Skips on an unperformed lookup rather than gating on a file. It used to be
    `skipif(not hp.db exists)`, which was wrong twice over: `conf/oak_config.yaml`
    maps `HP: ols:hp`, so HP resolves over the network and that database is
    never consulted — the gate neither enabled the lookup nor predicted it. The
    real failure mode is a flaky or rate-limited OLS, which made this test fail
    intermittently (measured: 1 in 3 full-file runs) with `assert False` on a
    line about otitis, for a reason that had nothing to do with the assertion.
    A test that cannot tell "the label is wrong" from "I could not look it up"
    reports the network as a code defect.
    """
    from dismech.phenotype_distribution import check_terms

    def mutate(data):
        data["disease"]["disease_term"]["term_id"] = "HP:0410017"

    issues = check_terms([_mutate(profile_set_path, mutate)])
    if unperformed := _unperformed_lookups(issues):
        pytest.skip(f"HP lookup did not happen: {unperformed[0]}")
    assert issues, "term check failed to flag a known-wrong CURIE"
    assert any("Otitis externa" in i.message for i in issues), (
        f"expected the real label to be reported; got {[i.message for i in issues]}"
    )


def test_example_terms_are_all_valid() -> None:
    """Errors only, and ungated.

    This was gated on `hp.db`, which it never needed: the example carries one
    ontology term, the set-level `MONDO:0020066`, and MONDO resolves through
    `ols:` over the network. The gate was inherited from the test beside it and
    silently skipped a check that would have run.

    Errors only, because a network-backed lookup that could not be performed is
    reported as a WARNING — deliberately, since it is not evidence the term is
    wrong. Asserting on warnings would make the suite fail on a flaky
    connection, the same conflation the severity split exists to avoid, and
    `just qc` draws the line in the same place.
    """
    from dismech.phenotype_distribution import check_terms

    errors = [
        i
        for i in check_terms(discover_collections(_all_paths()))
        if i.severity == "ERROR"
    ]
    assert not errors, [i.format() for i in errors]


def test_written_cache_files_satisfy_the_frontmatter_contract(
    tmp_path: Path,
) -> None:
    collections = _renderable_collections()
    written, _pruned = write_cache_files(collections, tmp_path)
    assert written
    assert frontmatter_main([str(tmp_path)]) == 0


def test_write_cache_files_is_idempotent(tmp_path: Path) -> None:
    collections = _renderable_collections()
    write_cache_files(collections, tmp_path)
    first = {p.name: p.read_bytes() for p in tmp_path.glob("*.md")}
    write_cache_files(collections, tmp_path)
    second = {p.name: p.read_bytes() for p in tmp_path.glob("*.md")}
    assert first == second


def test_no_temporary_files_left_behind(tmp_path: Path) -> None:
    write_cache_files(_renderable_collections(), tmp_path)
    assert not list(tmp_path.glob("*.tmp"))


# ---------------------------------------------------------------------------
# Repository hygiene
# ---------------------------------------------------------------------------


def test_example_profiles_are_not_citable_from_kb_entries() -> None:
    """The worked example is a demonstration and must stay uncited.

    It is still linted and rendered so the tooling is exercised, but its
    numbers come from a research artifact on a feature branch rather than a
    published cohort, so nothing under kb/ may cite one and no cache file for
    one may be committed.
    """
    example_ids = {
        profile["profile_id"]
        for coll in discover_collections(_example_paths())
        for profile in coll.profiles
    }
    assert example_ids

    cited = set()
    for path in (REPO_ROOT / "kb").rglob("*.yaml"):
        text = path.read_text(encoding="utf-8")
        if "PHENODIST:" not in text:
            continue
        for rid in example_ids:
            if f"PHENODIST:{rid}" in text:
                cited.add((path.name, rid))
    assert not cited, f"kb entries cite example profiles: {sorted(cited)}"

    committed = [
        p.name
        for rid in example_ids
        if (p := REPO_ROOT / "references_cache" / f"PHENODIST_{rid}.md").exists()
    ]
    assert not committed, f"example cache files are committed: {sorted(committed)}"


# ---------------------------------------------------------------------------
# EHR-derived profiles
# ---------------------------------------------------------------------------


@pytest.fixture()
def profile_set_path() -> Path:
    return EXAMPLES_DIR / "charmpheno_population_eds.yaml"


def test_profiles_carry_no_model_layer() -> None:
    """The model layer is gone, and should not come back by accident.

    An earlier draft grew component counts, inference methods, per-domain
    reliability and cohort arms. That is model evaluation rather than
    disease-page content, and the fastest-moving part of the pipeline — a
    curation schema encoding it needs revising every time the models move.
    Anything model-specific now goes in `profile_source.profile_metadata`.
    """
    sv = SchemaView(str(SCHEMA_PATH))
    classes = set(sv.all_classes())
    gone = {
        "LatentPhenotypeModel",
        "LatentPhenotype",
        "WeightedFeature",
        "ModelProperty",
        "ModelDomain",
        "DomainReliability",
        "ReliabilityReadout",
        "CohortArm",
        "ComponentIndexRange",
        "IdentityAttestation",
        # The literature/statistical shape, cut as out of scope for this
        # iteration. Its residue is the same hazard as the model layer's: prose
        # describing a second tree root that no longer exists sends a curator
        # looking for a payload the schema cannot validate.
        "PhenotypeDistributionCollection",
        "PhenotypeDistributionRecord",
        "DistributionFamilyEnum",
        "IdentificationStep",
        "DistributionBin",
        "DismechBinding",
    }
    assert not (classes & gone), f"model layer reintroduced: {sorted(classes & gone)}"

    slots = set(sv.class_slots("Profile")) | set(sv.class_slots("ProfileSet"))
    assert "profile_weight" in slots
    # The word the data producer asked this schema to stop using for a weight.
    for name in slots:
        assert "prevalence" not in name, f"{name} reintroduces `prevalence`"

    # Names alone are not enough. The deletion was complete in the class and
    # slot definitions while the schema's own prose still described the removed
    # layer end to end — including a de-OMOP'd class whose docstring still said
    # "One OMOP concept", one line above the guard meant to prevent that. Prose
    # drift is this PR's dominant defect mode, so the guard reads prose.
    prose = [sv.schema.description or ""]
    for name, cls in sv.all_classes().items():
        prose.append(f"{name}: {cls.description or ''}")
    for name, slot in sv.all_slots().items():
        prose.append(f"{name}: {slot.description or ''}")
    for name, enum in sv.all_enums().items():
        prose.append(f"{name}: {enum.description or ''}")
        for pv_name, pv in (enum.permissible_values or {}).items():
            prose.append(f"{name}.{pv_name}: {pv.description or ''}")
    blob = "\n".join(prose)

    stale = sorted(n for n in gone if n in blob)
    assert not stale, f"schema prose still describes deleted classes: {stale}"
    dead = (
        "model_properties",
        "feature_namespace",
        "domain_role",
        # Not slot names but the vocabulary the deleted binding carried. The
        # `TOOL_EXPORTED` tier said records "normally enter as PROPOSED
        # bindings pending review" — a published description pointing at a
        # status enum the schema no longer has. Matching deleted *names* could
        # not see it, because the word that survived was never a name here.
        "PROPOSED",
        "import_status",
    )
    for dead_slot in dead:
        assert dead_slot not in blob, (
            f"schema prose still refers to the deleted slot `{dead_slot}`"
        )


def test_schema_section_comments_head_something() -> None:
    """The last surface the deletion could hide in: YAML comments.

    Every guard above reads the schema through `SchemaView`, which discards
    comments at parse. So a deletion could — and did — leave eleven consecutive
    `# --- … ---` markers heading nothing, and strand the top-level `# Classes`
    banner 150 lines up inside the `slots:` block, where the next person to add
    a class would put it in the wrong section. Nothing structural breaks; the
    file just stops describing itself. This reads the raw text, which is the
    only way to see it.
    """
    lines = SCHEMA_PATH.read_text(encoding="utf-8").splitlines()

    def is_marker(ln: str) -> bool:
        """A `# --- name ---` section marker, not a `# -----` banner rule."""
        s = ln.strip()
        return s.startswith("# ---") and s.endswith("---") and bool(s[5:-3].strip(" -"))

    empty: list[str] = []
    for i, line in enumerate(lines):
        if not is_marker(line):
            continue
        # A marker must be followed by at least one definition before the next
        # marker, the next banner, or the end of the file.
        for nxt in lines[i + 1 :]:
            if is_marker(nxt) or nxt.startswith("#"):
                empty.append(f"{i + 1}: {line.strip()}")
                break
            if nxt.strip() and not nxt.lstrip().startswith("#"):
                break
        else:
            empty.append(f"{i + 1}: {line.strip()}")
    assert not empty, f"section markers heading no definition: {empty}"

    # And the top-level banners must sit above the block they name.
    for banner, key in (
        ("# Enums", "enums:"),
        ("# Slots", "slots:"),
        ("# Classes", "classes:"),
    ):
        b = [i for i, ln in enumerate(lines) if ln.strip() == banner]
        k = [i for i, ln in enumerate(lines) if ln.rstrip() == key]
        assert len(b) == 1 and len(k) == 1, f"expected one {banner} and one `{key}`"
        assert 0 < k[0] - b[0] < 6, (
            f"the `{banner}` banner is at line {b[0] + 1} but `{key}` opens at "
            f"line {k[0] + 1}; the banner has drifted away from its block"
        )


def test_codes_are_generic_with_a_declared_vocabulary() -> None:
    """No OMOP-shaped field names.

    Hard-coding `concept_id`/`concept_name` quietly makes OMOP the only
    representable case; data may arrive already coded in ICD or LOINC. The
    lesson that survives is narrower — do not put a source-vocabulary CURIE in a
    code field — so the code stays opaque and the vocabulary is declared.
    """
    sv = SchemaView(str(SCHEMA_PATH))
    code_slots = set(sv.class_slots("WeightedCode"))
    assert {"code", "code_label", "code_weight"} <= code_slots
    assert not {"concept_id", "concept_name"} & code_slots

    dist_slots = set(sv.class_slots("CodeDistribution"))
    assert "code_vocabulary" in dist_slots
    assert sv.get_slot("code_vocabulary").range == "CodeVocabularyEnum"
    assert sv.induced_slot("code_vocabulary", "CodeDistribution").required


def test_lint_flags_weights_summing_above_one(profile_set_path: Path) -> None:
    def mutate(data):
        data["profiles"][0]["code_distributions"][0]["weighted_codes"][0][
            "code_weight"
        ] = 0.99

    assert "above 1.0" in _error_messages(_mutate(profile_set_path, mutate))


def test_lint_warns_when_a_short_distribution_is_not_marked_truncated(
    profile_set_path: Path,
) -> None:
    """A top-N export and a distribution that lost mass look identical.

    Only `truncated` tells them apart, so weights that fall short without it
    should say so rather than be read as a complete distribution.
    """

    def mutate(data):
        data["profiles"][0]["code_distributions"][0].pop("truncated")

    assert "not marked `truncated: true`" in _warning_messages(
        _mutate(profile_set_path, mutate)
    )


def test_lint_flags_a_duplicated_code(profile_set_path: Path) -> None:
    def mutate(data):
        codes = data["profiles"][0]["code_distributions"][0]["weighted_codes"]
        codes.append(dict(codes[0]))

    assert "twice" in _error_messages(_mutate(profile_set_path, mutate))


def test_the_schema_declares_no_reverse_pointer_to_kb_entries() -> None:
    """A profile set names no dismech entry, in either direction.

    An earlier draft had each profile declare a `dismech_bindings` block naming
    the entry and section it belonged to. Nothing else in this repo points that
    way: ORPHA, ClinGen, ICEES and NCIT are all cited *by* an entry and know
    nothing about it. A source-side pointer is a second place for the same fact
    to be wrong, and the association a set does need — which disease — is the
    MONDO term it already carries.
    """
    sv = SchemaView(str(SCHEMA_PATH))
    names = set(sv.all_classes()) | set(sv.all_slots())
    reverse = {
        "DismechBinding",
        "dismech_bindings",
        "target_entry",
        "target_kind",
        "target_section",
        "evidence_reference",
    }
    assert not (names & reverse), (
        f"reverse pointer reintroduced: {sorted(names & reverse)}"
    )


def test_profiles_export_through_the_citation_bridge(
    profile_set_path: Path, tmp_path: Path
) -> None:
    """A profile becomes citable the same way every structured source does.

    A disease entry cites `PHENODIST:<id>` and quotes a row — the mechanism
    ORPHA, ClinGen, ICEES and NCIT already use, rather than a bridge of this
    schema's own.
    """
    coll = load_collection(profile_set_path)
    entry = profile_cache_entry(coll, coll.profiles[1])
    assert entry.reference_id == "PHENODIST:CHARMPHENO-EDS-DYSAUTONOMIA-001"
    assert entry.filename() == "PHENODIST_CHARMPHENO-EDS-DYSAUTONOMIA-001.md"
    # Rows are quotable substrings — the contract curator snippets depend on.
    row = "| 4159659 | Postural orthostatic tachycardia syndrome | 0.11381 |"
    assert row in entry.body
    assert "| Vocabulary | OMOP_CONCEPT_ID |" in entry.body
    # The disease is declared once for the set, but each cache file is read
    # alone, so it has to carry the disease it is about.
    assert "MONDO:0020066" in entry.body
    assert entry.title.endswith("in Ehlers-Danlos Syndrome")


def test_profile_rendering_is_deterministic(profile_set_path: Path) -> None:
    coll = load_collection(profile_set_path)
    first = [render_profile_body(coll, p) for p in coll.profiles]
    second = [
        render_profile_body(load_collection(profile_set_path), p) for p in coll.profiles
    ]
    assert first == second


def test_a_profile_weight_requires_its_denominator(profile_set_path: Path) -> None:
    """A share without a denominator is silently incomparable.

    The reason this slot is `profile_weight` rather than `prevalence` is
    denominator hygiene, so leaving the denominator to free-text prose gave up
    the point: a share over a whole corpus and a share over one disease arm
    differ by orders of magnitude and look identical.
    """

    def mutate(data):
        data["profile_source"].pop("weight_basis")

    assert "weight_basis" in _error_messages(_mutate(profile_set_path, mutate))


def test_profile_weights_cannot_exceed_the_mass_they_divide(
    profile_set_path: Path,
) -> None:
    """Only an upper bound is meaningful.

    Real exports are top-N, so shares falling short of 1 is the normal case —
    but shares totalling more than the fit's whole mass is the same
    impossibility the per-distribution check already catches.
    """

    def mutate(data):
        data["profiles"][0]["profile_weight"] = 0.7
        data["profiles"][1]["profile_weight"] = 0.7

    assert "above 1.0" in _error_messages(_mutate(profile_set_path, mutate))


def test_the_schema_carries_no_orphan_definitions() -> None:
    """A deleted class must take its slots with it.

    The model layer was removed class by class, and `DomainReliability`'s
    cross-validation slots plus `ModelProperty`'s value slot outlived their only
    owners — as did `TermDescriptor`, a second unused spelling of the descriptor
    pattern sitting beside the `term_id`/`term_label` shape actually in use.
    `gen-doc` publishes orphans, so a reader sees contract where there is
    residue, and the prose guard cannot see them: a slot wired to nothing is
    neither a stale name in prose nor a class still in `all_classes()`.
    """
    sv = SchemaView(str(SCHEMA_PATH))

    used = {slot for cn in sv.all_classes() for slot in sv.class_slots(cn)}
    orphan_slots = sorted(set(sv.all_slots()) - used)
    assert not orphan_slots, f"slots defined but used by no class: {orphan_slots}"

    ranges = {
        sv.induced_slot(slot, cn).range
        for cn in sv.all_classes()
        for slot in sv.class_slots(cn)
    }
    roots = {c for c in sv.all_classes() if sv.get_class(c).tree_root}
    orphan_classes = sorted(
        c
        for c in sv.all_classes()
        if c not in ranges and c not in roots and not sv.class_children(c)
    )
    assert not orphan_classes, f"classes reachable from nothing: {orphan_classes}"


def test_a_distribution_description_cannot_misstate_its_own_sum(
    profile_set_path: Path,
) -> None:
    """The one claim in the file that is checkable arithmetic, checked.

    "the weights sum to ~0.73" drifted twice by hand — a code was added and the
    sentence was not. Unlike a prose keyword, this is a number derivable from
    the same file, so it does not need to be trusted.
    """

    def mutate(data):
        dist = data["profiles"][0]["code_distributions"][0]
        dist["description"] = "Top codes, so the weights sum to ~0.42 rather than 1."

    assert "they sum to 0.72693" in _error_messages(_mutate(profile_set_path, mutate))

    # A description making no such claim is untouched.
    def silent(data):
        dist = data["profiles"][0]["code_distributions"][0]
        dist["description"] = "The eight highest-probability codes."

    assert lint_collections([_mutate(profile_set_path, silent)]).errors == []

    # Sentence-final, which both phrasings above dodge. `[\d.]+` captured the
    # period too and handed `float()` "0.73.", turning a lint finding into a
    # traceback out of a `just qc` gate — a worse failure than the drift.
    def trailing_period_correct(data):
        dist = data["profiles"][0]["code_distributions"][0]
        dist["description"] = "Top codes, so the weights sum to ~0.73."

    assert (
        lint_collections([_mutate(profile_set_path, trailing_period_correct)]).errors
        == []
    )

    def trailing_period_wrong(data):
        dist = data["profiles"][0]["code_distributions"][0]
        dist["description"] = "Top codes, so the weights sum to ~0.42."

    assert "they sum to 0.72693" in _error_messages(
        _mutate(profile_set_path, trailing_period_wrong)
    )


def test_the_sum_claim_is_judged_at_the_precision_it_was_written_to(
    profile_set_path: Path,
) -> None:
    """A guard against drift must never contradict correct arithmetic.

    The first version used a fixed `>= 0.005`, which is *exactly* the largest
    legitimate rounding error for a two-decimal claim — so the boundary case,
    a distribution summing to 0.7350 correctly written "~0.74", was reported
    as a misstatement. The live example sat 0.0001 from that edge. The same
    fixed number was simultaneously far too strict one digit up: "~0.7" is the
    right way to describe 0.7269, and it was flagged.

    Half a unit in the last written place is what makes both come out right,
    so both directions are pinned here.
    """

    def with_codes(weights, text):
        def mutate(data):
            dist = data["profiles"][0]["code_distributions"][0]
            dist["weighted_codes"] = [
                {"code": str(i), "code_label": f"c{i}", "code_weight": w}
                for i, w in enumerate(weights)
            ]
            dist["description"] = text

        return _mutate(profile_set_path, mutate)

    # Exactly halfway: 0.735 rounds to 0.74, so the claim is correct.
    assert lint_collections([with_codes([0.5, 0.235], "sum to ~0.74")]).errors == []
    # And rounding the other way is equally correct at that precision.
    assert lint_collections([with_codes([0.5, 0.235], "sum to ~0.73")]).errors == []
    # A whole unit out at that precision is still a misstatement.
    assert "they sum to 0.73500" in _error_messages(
        with_codes([0.5, 0.235], "sum to ~0.75")
    )

    # One decimal is judged to one decimal: 0.72693 is "~0.7", not an error.
    assert lint_collections([with_codes([0.5, 0.22693], "sum to ~0.7")]).errors == []
    assert "they sum to 0.72693" in _error_messages(
        with_codes([0.5, 0.22693], "sum to ~0.6")
    )


def test_a_sum_claim_is_checked_with_or_without_the_tilde(
    profile_set_path: Path,
) -> None:
    """The opt-in is the claim, not the punctuation.

    The switch was `~` alone, so "the weights sum to 0.42" — a plain, natural
    way to write it — bought silence. Silence from a guard is indistinguishable
    from a pass, which makes that the worst possible failure mode for a check
    whose whole job is to notice drift.

    A decimal point is still required, and that is the other half of the same
    decision: "do not sum to 1" and "rather than 1" are both live phrasings in
    this repo's descriptions, and matching a bare integer would read a negation
    as a claim. It also drops integer claims, which under the half-a-unit rule
    would have carried a useless +/- 0.5 tolerance.
    """

    def described(text):
        def mutate(data):
            data["profiles"][0]["code_distributions"][0]["description"] = text

        return _mutate(profile_set_path, mutate)

    # No tilde, wrong number: caught.
    assert "they sum to 0.72693" in _error_messages(
        described("The weights sum to 0.42")
    )
    # No tilde, right number: silent.
    assert lint_collections([described("The weights sum to 0.73")]).errors == []

    # A bare integer is not a claim. The discriminating case is a heavily
    # truncated distribution, because that is where a matched "1" would land
    # outside the +/- 0.5 an integer claim implies and be reported as a
    # misstatement — of a sentence that says the opposite. A mutant regex
    # allowing bare integers passes every milder phrasing, so those prove
    # nothing; this one is the test.
    def truncated_to(total, text):
        def mutate(data):
            dist = data["profiles"][0]["code_distributions"][0]
            dist["weighted_codes"] = [
                {"code": "1", "code_label": "c", "code_weight": total}
            ]
            dist["description"] = text

        return _mutate(profile_set_path, mutate)

    assert (
        lint_collections(
            [truncated_to(0.4, "The top codes only, so the weights do not sum to 1")]
        ).errors
        == []
    )
    # The live example's phrasing, kept as a regression pin and *not* part of
    # the mutation argument: `re.search` takes `~0.4` before it ever reaches
    # the trailing `1`, so this stays silent under the permissive regex too.
    assert (
        lint_collections(
            [truncated_to(0.4, "Top codes, so the weights sum to ~0.4 rather than 1")]
        ).errors
        == []
    )


def test_backticked_identifiers_in_schema_prose_resolve() -> None:
    """A deleted slot must not survive as an option in someone's prose.

    Four deletions in this schema have now left residue, each one layer further
    out than the last guard could see: classes, then slots, then descriptions
    mentioning removed machinery, then this — a class description still offering
    `latent_phenotype` as an alternative that no longer exists, three cleanup
    commits after the slot went. `gen-doc` publishes class descriptions, so a
    reader is handed a choice the schema cannot honour.

    Scoped to backticked lowercase tokens, which in this file are how slots are
    referred to. An earlier version required an underscore, which left 62
    single-word slots invisible — including `phenotype`, the other half of the
    very sentence that prompted this check: had the deletion gone the other way,
    the guard would have stayed silent.

    The allowlist is names that are real but live elsewhere. All five are the
    same kind — cross-schema or cross-tool references — and that sameness is the
    bar. An allowlist accumulating *different* kinds of exception is the signal
    this check has outlived its scope; one growing within a single category is
    not. Entries are also asserted to be live, so an exemption cannot outlive
    the prose that needed it, which is the residue pattern this file keeps
    producing.
    """
    import re as _re

    sv = SchemaView(str(SCHEMA_PATH))
    known: set[str] = (
        set(sv.all_slots())
        | set(sv.all_classes())
        | set(sv.all_enums())
        | set(sv.all_types())
    )
    for enum in sv.all_enums().values():
        known |= set(enum.permissible_values or {})

    elsewhere = {
        # Real slots, but in the main dismech schema rather than this one.
        "prevalence",
        # dismech's `Term` spells its slots `id`/`label`; this schema spells
        # them `term_id`/`term_label`. The `Term` description names both to
        # record the collision, so `label` resolves there and not here. (`id`
        # needs no exemption — `Document` happens to have one.)
        "label",
        # A LinkML metaslot, and an export field of an external tool.
        "see_also",
        "metadata",
    }

    descriptions: list[tuple[str, str]] = [("schema", sv.schema.description or "")]
    for name, cls in sv.all_classes().items():
        descriptions.append((f"class {name}", cls.description or ""))
    for name, slot in sv.all_slots().items():
        descriptions.append((f"slot {name}", slot.description or ""))

    dangling: list[str] = []
    seen: set[str] = set()
    for where, text in descriptions:
        for token in _re.findall(r"`([a-z][a-z0-9_]*)`", text):
            seen.add(token)
            if token not in known and token not in elsewhere:
                dangling.append(f"{where} -> `{token}`")
    assert not dangling, (
        "schema prose references identifiers that resolve to nothing: "
        f"{sorted(set(dangling))}"
    )

    # An exemption that matches nothing is the same residue this guard exists to
    # catch, one level up. `metadata` was exactly that under the narrower
    # pattern: allowlisted, and unreachable.
    stale = sorted(elsewhere - seen)
    assert not stale, (
        f"allowlist entries with no prose references, so the exemption has "
        f"outlived the text that needed it: {stale}"
    )

    # And the same check one class wider. The identifier pattern above cannot
    # see a backticked *path*, because slashes and hyphens fall outside it —
    # which is how `docs/proposals/dismech-profiles` survived in a class
    # description pointing at a directory this repo has never had. A reader
    # follows it and finds nothing, the same failure as a dangling slot name.
    missing = [
        f"{where} -> `{token}`"
        for where, text in descriptions
        for token in _re.findall(r"`([A-Za-z0-9_./-]+/[A-Za-z0-9_./-]+)`", text)
        if not (REPO_ROOT / token).exists()
    ]
    assert not missing, f"schema prose points at paths that do not exist: {missing}"
