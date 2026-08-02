"""Tests for the statistical phenotype-distribution schema and tooling.

Covers three things: that the schema and its worked examples stay valid, that
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
    cache_entry,
    discover_collections,
    lint_collections,
    load_collection,
    render_body,
    summary_row,
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

TARGET_CLASS = "PhenotypeDistributionCollection"


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


def test_schema_loads_with_single_tree_root() -> None:
    sv = SchemaView(str(SCHEMA_PATH))
    roots = [name for name, cls in sv.all_classes().items() if cls.tree_root]
    assert roots == [TARGET_CLASS]


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


def test_frequency_class_values_match_native_frequency_enum() -> None:
    """Implied frequency bands must be the same bands dismech already uses."""
    sv = SchemaView(str(SCHEMA_PATH))
    native = SchemaView(str(NATIVE_SCHEMA_PATH))
    ours = sv.get_enum("FrequencyClassEnum").permissible_values
    theirs = native.get_enum("FrequencyEnum").permissible_values
    assert set(ours) == set(theirs)
    for name, pv in ours.items():
        assert pv.meaning == theirs[name].meaning


def test_model_layer_stays_at_the_common_denominator() -> None:
    """Model-family-specific structure belongs in `model_properties`.

    Latent phenotype model classes and their export shapes change fast. The
    escape hatch is what keeps a new one recordable without a schema change, so
    it must exist and the model class must carry it.
    """
    sv = SchemaView(str(SCHEMA_PATH))
    assert "ModelProperty" in sv.all_classes()
    model_slots = set(sv.class_slots("LatentPhenotypeModel"))
    # An allowlist, not a denylist: a denylist only catches the family-specific
    # slot names someone thought of today, and says nothing about the one added
    # next year. Adding a slot here should require justifying it as common to
    # every model class.
    allowed = {
        "model_name",
        "model_family",
        "version",
        "n_components",
        "component_count_inferred",
        "vocabulary_size",
        "covariate_formula",
        "inference_method",
        "hyperparameters",
        "model_properties",
        "training_cohort",
        "training_cohort_ref",
        "fit_metrics",
        "contains_patient_data",
        "artifact_url",
        "sha256",
        "software",
        "description",
        "notes",
    }
    assert model_slots == allowed, (
        "LatentPhenotypeModel slots changed; family-specific structure belongs "
        f"in model_properties. Unexpected: {sorted(model_slots - allowed)}"
    )

    # ModelDomain is the sibling the model layer can also grow sideways through,
    # so pin it too rather than leaving one door guarded and the other open.
    domain_slots = set(sv.class_slots("ModelDomain"))
    allowed_domain = {
        "domain_name",
        "vocabulary",
        "feature_namespace",
        "feature_namespace_detail",
        "n_features",
        "domain_role",
        "reliability",
        "description",
    }
    assert domain_slots == allowed_domain, (
        "ModelDomain slots changed; justify any addition as common to every "
        f"model class. Unexpected: {sorted(domain_slots - allowed_domain)}"
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
    assert result.n_records > 0


def _mutate(path: Path, mutator) -> Collection:
    coll = load_collection(path)
    coll = Collection(path=coll.path, data=copy.deepcopy(coll.data))
    mutator(coll.data)
    return coll


@pytest.fixture()
def cf_collection_path() -> Path:
    return EXAMPLES_DIR / "cystic_fibrosis_illustrative.yaml"


def _error_messages(coll: Collection) -> str:
    return " ".join(i.message for i in lint_collections([coll]).errors)


def test_lint_flags_duplicate_record_ids(cf_collection_path: Path) -> None:
    def mutate(data):
        data["distributions"][1]["record_id"] = data["distributions"][0]["record_id"]

    assert "duplicate record_id" in _error_messages(_mutate(cf_collection_path, mutate))


def test_lint_flags_mismatched_evidence_reference(cf_collection_path: Path) -> None:
    def mutate(data):
        data["distributions"][0]["dismech_bindings"][0]["evidence_reference"] = (
            "PHENODIST:something-else"
        )

    assert "does not match this record" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_flags_unresolvable_target_entry(cf_collection_path: Path) -> None:
    def mutate(data):
        data["distributions"][0]["dismech_bindings"][0]["target_entry"] = "No_Such_Disease"

    assert "does not" in _error_messages(_mutate(cf_collection_path, mutate))


def test_lint_flags_interval_not_bracketing_point_estimate(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        data["distributions"][0]["distribution"]["summary"]["point_estimate"] = 0.99

    assert "above the interval upper bound" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_flags_frequency_band_contradicting_point_estimate(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        data["distributions"][0]["implied_frequency_class"] = "OCCASIONAL"

    assert "falls in the VERY_FREQUENT band" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_flags_self_contradictory_identity_attestation(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        att = data["cohorts"][0]["identity_attestation"]
        att["unique_person_count"] = 900

    assert "one row per person" in _error_messages(_mutate(cf_collection_path, mutate))


def test_lint_flags_matrix_dimension_mismatch() -> None:
    path = EXAMPLES_DIR / "charmpheno_population_eds.yaml"

    def mutate(data):
        for record in data["distributions"]:
            for param in record["distribution"].get("parameters") or []:
                if param.get("matrix_value"):
                    param["matrix_value"]["values"].pop()
                    return

    assert "entries but lists" in _error_messages(_mutate(path, mutate))


def test_lint_flags_latent_mixture_without_a_model() -> None:
    path = EXAMPLES_DIR / "charmpheno_population_eds.yaml"

    def mutate(data):
        del data["model"]

    assert "declares no `model`" in _error_messages(_mutate(path, mutate))


# ---------------------------------------------------------------------------
# Reference-cache export
# ---------------------------------------------------------------------------


def test_summary_row_column_contract(cf_collection_path: Path) -> None:
    """The quotable summary row's column order is part of the cache contract.

    Curators quote this row as an evidence snippet, so reordering or dropping a
    column silently invalidates every snippet already quoted from it.
    """
    coll = load_collection(cf_collection_path)
    record = coll.records[0]
    row = summary_row(record)
    cells = [c.strip() for c in row.strip().strip("|").split("|")]
    assert cells == [
        "CF-PI-PROPORTION-001",
        "PHENOTYPE_PROPORTION",
        "BETA",
        "0.862",
        "95% CREDIBLE_EQUAL_TAILED 0.842-0.881",
        "n=1240",
        "whole cohort",
    ]


def test_render_is_deterministic(cf_collection_path: Path) -> None:
    coll = load_collection(cf_collection_path)
    record = coll.records[0]
    assert render_body(coll, record) == render_body(coll, record)


def test_cache_entry_identifier_and_filename(cf_collection_path: Path) -> None:
    coll = load_collection(cf_collection_path)
    entry = cache_entry(coll, coll.records[0])
    assert entry.reference_id == "PHENODIST:CF-PI-PROPORTION-001"
    assert entry.filename() == "PHENODIST_CF-PI-PROPORTION-001.md"
    assert entry.title.endswith("in Cystic Fibrosis")


def test_rendered_body_contains_the_quotable_summary_row(
    cf_collection_path: Path,
) -> None:
    coll = load_collection(cf_collection_path)
    record = coll.records[0]
    assert summary_row(record) in render_body(coll, record)


def test_table_cells_never_contain_unescaped_pipes(cf_collection_path: Path) -> None:
    """A stray pipe in free text must not break a quotable row."""
    coll = load_collection(cf_collection_path)
    coll = Collection(path=coll.path, data=copy.deepcopy(coll.data))
    coll.data["distributions"][0]["measure_description"] = "a | b | c"
    body = render_body(coll, coll.records[0])
    line = next(ln for ln in body.splitlines() if ln.startswith("| Measure description"))
    assert line.count("|") - line.count(r"\|") == 3  # two delimiters + separator


def test_suppressed_bins_render_distinguishably_from_zero() -> None:
    """A withheld bin and a reported zero must not look the same in the cache."""
    path = EXAMPLES_DIR / "charmpheno_population_eds.yaml"
    coll = load_collection(path)
    record = next(
        r for r in coll.records if r["record_id"] == "CHARMPHENO-EDS-T96-THETA-001"
    )
    body = render_body(coll, record)
    bin_rows = [ln for ln in body.splitlines() if ln.startswith("| [0.")]
    suppressed = [ln for ln in bin_rows if ln.rstrip().endswith("true |")]
    reported_zero = [ln for ln in bin_rows if "| 0 |" in ln]
    assert suppressed, bin_rows
    assert reported_zero, bin_rows
    assert not set(suppressed) & set(reported_zero)


def test_illustrative_collections_cannot_be_rendered_into_the_cache(
    tmp_path: Path,
) -> None:
    """Synthetic numbers must not be able to become citable, even by mistake."""
    illustrative = [
        c
        for c in discover_collections(_all_paths())
        if c.data.get("provenance_tier") == "ILLUSTRATIVE"
    ]
    assert illustrative, "expected at least one illustrative example collection"
    with pytest.raises(ValueError, match="ILLUSTRATIVE"):
        write_cache_files(illustrative, tmp_path)
    assert not list(tmp_path.glob("*.md"))


def test_write_cache_files_prunes_orphaned_records(tmp_path: Path) -> None:
    """A renamed or deleted record must not leave a citable cache file behind."""
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


@pytest.fixture()
def eds_collection_path() -> Path:
    return EXAMPLES_DIR / "charmpheno_population_eds.yaml"


def _warning_messages(coll: Collection) -> str:
    return " ".join(i.message for i in lint_collections([coll]).warnings)


def test_lint_warns_when_a_model_declares_no_domains(eds_collection_path: Path) -> None:
    """Omitting `domains` entirely must not be quieter than getting it wrong.

    Guarding only the declaring side caught the careful curator and missed the
    careless one: a collection that declared domains and forgot the enum warned,
    while one that omitted the block said nothing.
    """

    def drop(data):
        data.pop("domains")

    assert "declares no `domains`" in _warning_messages(
        _mutate(eds_collection_path, drop)
    )

    def empty(data):
        data["domains"] = []

    assert "declares no `domains`" in _warning_messages(
        _mutate(eds_collection_path, empty)
    )


def test_lint_warns_when_a_domain_omits_its_feature_namespace(
    eds_collection_path: Path,
) -> None:
    def mutate(data):
        for domain in data["domains"]:
            domain.pop("feature_namespace", None)

    assert "does not declare a `feature_namespace`" in _warning_messages(
        _mutate(eds_collection_path, mutate)
    )


def test_lint_errors_on_a_feature_referencing_an_undeclared_domain(
    eds_collection_path: Path,
) -> None:
    """`domain_name` is how a feature reaches its namespace; a dangling ref breaks it."""

    def mutate(data):
        for record in data["distributions"]:
            for feature in (record.get("latent_phenotype") or {}).get(
                "top_features"
            ) or []:
                feature["domain_name"] = "nonexistent"
                return

    assert "is not declared in `domains`" in _error_messages(
        _mutate(eds_collection_path, mutate)
    )


def test_lint_warns_on_an_ambiguous_feature_namespace(
    eds_collection_path: Path,
) -> None:
    """With more than one domain declared, an unlabelled feature has no namespace."""

    def mutate(data):
        for record in data["distributions"]:
            for feature in (record.get("latent_phenotype") or {}).get(
                "top_features"
            ) or []:
                feature.pop("domain_name", None)
                return

    assert "its namespace is ambiguous" in _warning_messages(
        _mutate(eds_collection_path, mutate)
    )


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

    assert not (coded - documented), f"docs omit verified prefixes: {sorted(coded - documented)}"
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


def test_prose_domain_role_lists_are_complete() -> None:
    """Any prose list of `domain_role` values must name all of them.

    This omission has now been made twice from the same source text: `CLAUDE.md`
    and `docs/phenotype-distributions.md` both listed four of five, dropping
    `UNDETERMINED`. That is not a tidiness problem. The four survivors are all
    *assessed* verdicts, so a curator with an unevaluated domain and no
    `UNDETERMINED` in front of them reaches for `EXCLUDED`, which asserts the
    domain was assessed and degraded performance — a claim they have no basis
    for and nothing downstream can tell apart from a real one.

    The check is deliberately wording-agnostic: it finds parenthesised
    slash-separated backticked runs anywhere in either file and requires any run
    already naming two or more roles to name them all. Prose can be rewritten
    freely; it just cannot go back to being partial.

    Be precise about what that enforces, because it is weaker than it sounds for
    `CLAUDE.md`. The matched group is the whole parenthetical, and that one names
    `UNDETERMINED` twice — in the slash-list and again in the inline "use
    `UNDETERMINED` … *not* `EXCLUDED`" contrast. So the enforced property is "the
    parenthetical names every value somewhere", not "each slash-list is
    complete": deleting it from the list alone leaves the set intact and the
    guard green. That is the property worth having. The harm is a curator meeting
    four assessed verdicts and no way to say "not assessed", and a reader of that
    parenthetical still meets all five whichever half carries them. Tightening
    the regex to per-list granularity would buy precision this failure mode does
    not need, at the cost of brittleness against ordinary rewording — which is
    the thing this design is trying to avoid.
    """
    import re

    roles = set(SchemaView(str(SCHEMA_PATH)).get_enum("DomainRoleEnum").permissible_values)

    def enumerations(text: str) -> list[set[str]]:
        """Every parenthesised run in `text` that is enumerating `DomainRoleEnum`.

        Two matches qualify a run, not one: `PRIMARY` alone is a plausible word
        in some unrelated list, but two role values together are not a
        coincidence.
        """
        found = []
        # Newlines are in the class because both files wrap these lists mid-run.
        for group in re.findall(r"\(([^()]*`[A-Z_]+`[^()]*)\)", text, flags=re.DOTALL):
            named = {v for v in re.findall(r"`([A-Z_]+)`", group) if v in roles}
            if len(named) >= 2:
                found.append(named)
        return found

    def assert_complete(where: Path, source: str, text: str) -> list[set[str]]:
        # `where` is threaded through rather than closed over: this is called
        # from inside a loop that rebinds `path`, and a late-binding closure is
        # how a helper like this quietly starts naming the wrong file.
        found = enumerations(text)
        for named in found:
            assert named == roles, (
                f"{where} ({source}) enumerates domain_role but omits "
                f"{sorted(roles - named)}; list every value or drop the parenthetical"
            )
        return found

    for path in (CLAUDE_MD_PATH, DOCS_PATH):
        # The working tree is checked so a curator editing prose sees their own
        # drift before committing it — but only for completeness, never as the
        # anchor. Anchoring here is what makes "delete the list" a green escape
        # from "keep the list current", and it would also make the guard hostage
        # to any tooling that mutates a checkout: an agent harness in this org
        # blanks this repo's `CLAUDE.md` section, which would fire for a reason
        # having nothing to do with the docs and invite whoever hit it to weaken
        # a working guard.
        assert_complete(
            path, "working tree", (REPO_ROOT / path).read_text(encoding="utf-8")
        )

        # Everything that actually gates is asserted against the committed blob:
        # it is what CI checks out and what readers get, and it is unaffected by
        # local mutation. Completeness belongs here too, not only on the anchor —
        # a mutated checkout whose worktree enumerations are empty would
        # otherwise leave the committed list unchecked, which is exactly the
        # exposure reading the blob exists to remove.
        committed = _committed_text(path)
        if committed is None:  # not a git checkout (sdist, vendored tree)
            continue
        assert assert_complete(path, "committed", committed), (
            f"{path} no longer enumerates domain_role anywhere in the committed "
            "blob. Either the guidance moved — point this test at its new home "
            "rather than deleting it — or a list eroded down to a single value, "
            "which falls under the two-value threshold and so reads here as no "
            "list at all."
        )


def test_a_yaml_that_is_not_a_collection_is_rejected(tmp_path: Path) -> None:
    """Silently treating the wrong file as an empty collection is worse than failing.

    The failure mode is a clean bill of health for a run that checked nothing:
    point the lint at the schema by mistake and it reports a record count and no
    findings, which reads exactly like success.
    """
    not_a_collection = tmp_path / "wrong.yaml"
    not_a_collection.write_text("id: https://example.org/x\nname: x\n", encoding="utf-8")
    with pytest.raises(ValueError, match="not a phenotype-distribution collection"):
        load_collection(not_a_collection)

    # The real schema is the file most likely to be passed by mistake.
    with pytest.raises(ValueError, match="not a phenotype-distribution collection"):
        load_collection(SCHEMA_PATH)

    # And a genuine collection still loads.
    assert load_collection(EXAMPLES_DIR / "cystic_fibrosis_illustrative.yaml").data


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


def test_lint_rejects_a_quote_not_in_the_cited_reference(
    cf_collection_path: Path,
) -> None:
    """Blocks laundering an unverified quote through the PHENODIST cache."""

    def mutate(data):
        line = data["distributions"][0]["evidence_lines"][1]
        line["has_evidence_items"][0]["item_value"] = "This sentence is not in the paper."

    assert "not a verbatim substring" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_rejects_a_quote_whose_reference_is_not_cached(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        line = data["distributions"][0]["evidence_lines"][1]
        line["has_evidence_items"][0]["reported_in"]["id"] = "PMID:99999999"

    assert "is not cached" in _error_messages(_mutate(cf_collection_path, mutate))


def test_zero_point_estimate_implies_no_frequency_band() -> None:
    """"Never observed" is a different claim from "<5%"."""
    from dismech.phenotype_distribution import _implied_band

    assert _implied_band(0.0) is None
    assert _implied_band(0.01) == "VERY_RARE"
    assert _implied_band(1.0) == "OBLIGATE"


def test_float_rendering_does_not_truncate_precision() -> None:
    """The quotable row must not silently round a tight parameter."""
    from dismech.phenotype_distribution import _fmt

    assert _fmt(5.272386501517754) == "5.272386501517754"
    assert _fmt(1.5071340388291068e-38) == "1.5071340388291068e-38"
    assert _fmt(1070.0) == "1070"


def _hp_db_available() -> bool:
    """Whether the local OAK HPO database is already downloaded."""
    return (Path.home() / ".data" / "oaklib" / "hp.db").exists()


@pytest.mark.skipif(not _hp_db_available(), reason="OAK HPO database not present")
def test_term_check_catches_a_wrong_curie(cf_collection_path: Path) -> None:
    """The regression guard for the CURIE that slipped through review.

    HP:0410017 is "Otitis externa". It reached this PR because nothing
    term-validated the new collections — `validate-terms-all` is hardcoded to
    `kb/disorders` with `-t Disease`.
    """
    from dismech.phenotype_distribution import check_terms

    def mutate(data):
        def walk(node):
            if isinstance(node, dict):
                if node.get("term_id") == "HP:0012236":
                    node["term_id"] = "HP:0410017"
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for i in node:
                    walk(i)

        walk(data)

    issues = check_terms([_mutate(cf_collection_path, mutate)])
    assert issues, "term check failed to flag a known-wrong CURIE"
    assert any("Otitis externa" in i.message for i in issues)


@pytest.mark.skipif(not _hp_db_available(), reason="OAK HPO database not present")
def test_example_terms_are_all_valid() -> None:
    from dismech.phenotype_distribution import check_terms

    issues = check_terms(discover_collections(_all_paths()))
    assert not issues, [i.format() for i in issues]


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


def test_example_collections_are_not_citable_from_kb_entries() -> None:
    """Illustrative records carry synthetic numbers and must stay uncited.

    They are still linted and rendered so the tooling is exercised, but nothing
    under kb/ may cite one, and no cache file for one may be committed.
    """
    example_ids = {
        record["record_id"]
        for coll in discover_collections(_example_paths())
        for record in coll.records
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
    assert not cited, f"kb entries cite illustrative records: {sorted(cited)}"

    committed = [
        p.name
        for rid in example_ids
        if (p := REPO_ROOT / "references_cache" / f"PHENODIST_{rid}.md").exists()
    ]
    assert not committed, f"illustrative cache files are committed: {sorted(committed)}"


# ---------------------------------------------------------------------------
# Cohort declaration, references, and identification chains
# ---------------------------------------------------------------------------


def test_lint_flags_unresolvable_cohort_ref(cf_collection_path: Path) -> None:
    def mutate(data):
        data["distributions"][0]["cohort_ref"] = "SYNTH-NO-SUCH-COHORT"

    assert "does not resolve to a cohort" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_flags_cohort_declared_both_inline_and_by_reference(
    cf_collection_path: Path,
) -> None:
    """One cohort, one source of truth — the duplication this slot removes."""

    def mutate(data):
        data["distributions"][0]["cohort"] = {"cohort_id": "SYNTH-CF-EHR"}

    assert "both `cohort` and `cohort_ref`" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_warns_when_a_record_re_declares_a_collection_cohort(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        record = data["distributions"][0]
        record.pop("cohort_ref")
        record["cohort"] = {"cohort_id": "SYNTH-CF-EHR", "n_individuals": 1240}

    assert "use `cohort_ref`" in _warning_messages(_mutate(cf_collection_path, mutate))


def test_referenced_cohort_renders_the_same_as_an_inline_one(
    cf_collection_path: Path,
) -> None:
    """Hoisting a shared cohort must not change a single cited byte.

    Cache bodies are quoted as evidence snippets, so a purely organizational
    move that altered the rendered text would silently invalidate citations.
    """
    coll = load_collection(cf_collection_path)
    record = coll.records[0]
    by_reference = render_body(coll, record)

    inlined = Collection(path=coll.path, data=copy.deepcopy(coll.data))
    target = inlined.records[0]
    target["cohort"] = copy.deepcopy(inlined.cohorts[target.pop("cohort_ref")])
    inlined.data.pop("cohorts")

    assert render_body(inlined, inlined.records[0]) == by_reference


def test_lint_flags_model_training_cohort_ref_that_does_not_resolve(
    eds_collection_path: Path,
) -> None:
    def mutate(data):
        data["model"]["training_cohort_ref"] = "NOPE"

    assert "training_cohort_ref" in _error_messages(_mutate(eds_collection_path, mutate))


def test_lint_warns_when_a_mapping_step_omits_its_relation(
    cf_collection_path: Path,
) -> None:
    """An exact-synonym crossing and a broad-match crossing are different cohorts."""

    def mutate(data):
        for step in data["cohorts"][0]["identification_steps"]:
            if step["step_role"] == "MAPPING":
                step.pop("mapping_relation")

    assert "mapping_relation" in _warning_messages(_mutate(cf_collection_path, mutate))


def test_lint_warns_when_an_expansion_step_omits_its_direction(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        for step in data["cohorts"][0]["identification_steps"]:
            if step["step_role"] == "EXPANSION":
                step.pop("expansion_direction")

    assert "expansion_direction" in _warning_messages(_mutate(cf_collection_path, mutate))


def test_lint_warns_when_a_component_belongs_to_no_arm(
    eds_collection_path: Path,
) -> None:
    """A component with no arm has an unstated denominator.

    The gated EDS components are estimated from 959 documents; read against the
    191,876-document corpus they mean something else entirely.
    """

    def mutate(data):
        for arm in data["cohorts"][0]["arms"]:
            if arm["arm_name"] == "eds":
                arm["associated_components"] = ["80"]
            # The background arm is the declared catch-all; without dropping the
            # flag it legitimately covers the components dropped above.
            arm.pop("backs_remaining_components", None)

    assert "not listed by any cohort arm" in _warning_messages(
        _mutate(eds_collection_path, mutate)
    )


def test_lint_flags_discrete_contradicting_its_family(cf_collection_path: Path) -> None:
    def mutate(data):
        data["distributions"][0]["distribution"]["discrete"] = True

    assert "contradicts family BETA" in _error_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_lint_warns_when_discrete_merely_restates_its_family(
    cf_collection_path: Path,
) -> None:
    def mutate(data):
        data["distributions"][0]["distribution"]["discrete"] = False

    assert "restates what family BETA already fixes" in _warning_messages(
        _mutate(cf_collection_path, mutate)
    )


def test_discrete_by_family_map_covers_the_enum() -> None:
    """The map and its four prose copies must not drift from the enum.

    A family added to the enum but not the map lands in the "support is open"
    bucket by omission: the lint silently stops checking it, and the six-value
    list repeated in the slot description, the warning text, `CLAUDE.md`, and
    the docs all become wrong with no signal.
    """
    from dismech.phenotype_distribution import _DISCRETE_BY_FAMILY

    sv = SchemaView(str(SCHEMA_PATH))
    families = set(sv.get_enum("DistributionFamilyEnum").permissible_values)

    unmapped = families - set(_DISCRETE_BY_FAMILY)
    open_support = {
        "EMPIRICAL",
        "KAPLAN_MEIER",
        "MIXTURE",
        "NONPARAMETRIC_QUANTILE",
        "OTHER",
        "UNIFORM",
    }
    assert unmapped == open_support, (
        "families whose support the family itself does not fix changed; update "
        "_DISCRETE_BY_FAMILY and every prose copy of the list together. "
        f"Unexpectedly unmapped: {sorted(unmapped - open_support)}; "
        f"unexpectedly mapped: {sorted(open_support - unmapped)}"
    )
    assert not set(_DISCRETE_BY_FAMILY) - families, (
        "_DISCRETE_BY_FAMILY maps a family the enum does not define: "
        f"{sorted(set(_DISCRETE_BY_FAMILY) - families)}"
    )

    # The prose copies name the same six, so a reader is never told a different
    # list from the one the lint enforces.
    slot_description = sv.get_slot("discrete").description or ""
    warning_text = _warning_messages(
        _mutate(
            EXAMPLES_DIR / "cystic_fibrosis_illustrative.yaml",
            lambda data: data["distributions"][0]["distribution"].update(discrete=False),
        )
    )
    sources: list[tuple[str, str]] = [
        ("the `discrete` slot description", slot_description),
        ("the lint warning", warning_text),
    ]
    # Prose files are read at HEAD, not from the working tree, for the reason
    # `_committed_text` exists: a checkout with unrelated local mutation would
    # otherwise fail this guard on content that is correct as committed. Its
    # sibling `test_prose_domain_role_lists_are_complete` was moved onto the
    # committed blob for exactly this, and reading the working tree here
    # reintroduced what that change removed.
    for label, path in (
        ("CLAUDE.md", CLAUDE_MD_PATH),
        ("the docs", DOCS_PATH),
    ):
        committed = _committed_text(path)
        if committed is None:  # not a git checkout (sdist, vendored tree)
            continue
        sources.append((label, committed))

    for source, text in sources:
        missing = [f for f in open_support if f not in text]
        assert not missing, f"{source} omits open-support families: {sorted(missing)}"


def test_lint_flags_an_arm_component_outside_the_model_range(
    eds_collection_path: Path,
) -> None:
    """Appending a bogus id, not replacing a real one.

    The reverse check only fires when a *record's* component goes unclaimed, so
    an arm listing all its real components plus one typo was silent. Bounds are
    the decidable half: "no record describes this id" is normal (the arm names
    twenty components, three have records), but an id outside the declared
    model's range is wrong however few records exist.
    """

    def append_bogus(data):
        for arm in data["cohorts"][0]["arms"]:
            if arm["arm_name"] == "eds":
                arm["associated_components"].append("T999-DOES-NOT-EXIST")

    assert "matches no component index" in _error_messages(
        _mutate(eds_collection_path, append_bogus)
    )

    def append_out_of_range(data):
        for arm in data["cohorts"][0]["arms"]:
            if arm["arm_name"] == "eds":
                arm["associated_components"].append("100")

    assert "outside the [0, 100) range" in _error_messages(
        _mutate(eds_collection_path, append_out_of_range)
    )


def test_arm_components_within_range_but_unreported_are_not_flagged(
    eds_collection_path: Path,
) -> None:
    """The normal case must stay silent, or the check is unusable.

    The EDS arm lists twenty foreground components and the collection reports
    records for three. Treating the other seventeen as dangling references would
    fire on correct data.
    """
    coll = load_collection(eds_collection_path)
    reported = {
        str(r["latent_phenotype"]["component_id"])
        for r in coll.records
        if r.get("latent_phenotype")
    }
    arm = next(a for a in coll.data["cohorts"][0]["arms"] if a["arm_name"] == "eds")
    assert len(set(arm["associated_components"]) - reported) > 10
    assert lint_collections([coll]).issues == []


def test_a_ranged_arm_claim_covers_components_without_enumerating_them(
    eds_collection_path: Path,
) -> None:
    """A background arm states `0-79` as a block, not eighty ids — and stays checked.

    The first attempt at this ergonomic was a `backs_remaining_components`
    boolean, which stood the reverse check down for the entire collection: a
    foreground component dropped from the `eds` arm then fell to the catch-all
    silently, attributing 959 people's component to 190,917. A range keeps the
    convenience and the check, so both halves are asserted here together.
    """

    def add_background_record(data):
        record = copy.deepcopy(data["distributions"][2])
        record["record_id"] = "CHARMPHENO-EDS-T12-CODEPROB-001"
        record["latent_phenotype"]["component_id"] = "12"
        record.pop("dismech_bindings", None)
        record.pop("evidence_lines", None)
        data["distributions"].append(record)

    # Covered by the background arm's 0-79 range: no complaint.
    assert "not listed by any cohort arm" not in _warning_messages(
        _mutate(eds_collection_path, add_background_record)
    )

    # And the substitution the range must not hide.
    def drop_a_foreground_component(data):
        add_background_record(data)
        for arm in data["cohorts"][0]["arms"]:
            if arm["arm_name"] == "eds":
                arm["associated_components"].remove("96")

    assert "component '96' is not listed by any cohort arm" in _warning_messages(
        _mutate(eds_collection_path, drop_a_foreground_component)
    )


def test_lint_flags_a_component_range_that_leaves_the_model(
    eds_collection_path: Path,
) -> None:
    """A bad range is reported once, as a range.

    Expanding first and validating after buried the actual mistake under a
    hundred out-of-range ids and twenty spurious overlaps with the arm next
    door, which is how a lint teaches people to ignore it.
    """

    def widen(data):
        for arm in data["cohorts"][0]["arms"]:
            if arm["arm_name"] == "background":
                arm["associated_component_ranges"][0]["range_upper"] = 200

    errors = lint_collections([_mutate(eds_collection_path, widen)]).errors
    assert len(errors) == 1, [e.message for e in errors]
    assert "leaves the [0, 100) range" in errors[0].message

    def invert(data):
        for arm in data["cohorts"][0]["arms"]:
            if arm["arm_name"] == "background":
                arm["associated_component_ranges"][0].update(
                    range_lower=79, range_upper=0
                )

    errors = lint_collections([_mutate(eds_collection_path, invert)]).errors
    assert len(errors) == 1, [e.message for e in errors]
    assert "lower bound exceeds its upper bound" in errors[0].message


def test_lint_flags_a_component_claimed_by_two_arms(
    eds_collection_path: Path,
) -> None:
    """Two arms claiming one component is two denominators for one number."""

    def overlap(data):
        for arm in data["cohorts"][0]["arms"]:
            if arm["arm_name"] == "eds":
                arm["associated_components"].append("12")

    assert "claimed by both arm" in _error_messages(
        _mutate(eds_collection_path, overlap)
    )
