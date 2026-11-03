"""Tests for the grouping gene-level GO activity audit.

They pin the verdict logic: which genes count as causal, how evidence codes
rank, that NOT annotations never support a member, and that an ai-gene-review
core term is reported without changing the verdict. The QuickGO and UniProt
lookups are stubbed, so nothing here touches the network.
"""

from pathlib import Path

import yaml

from scripts import grouping_gene_go_audit as audit

ROOTS = ["GO:0005216", "GO:0099106"]


def _write_yaml(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False))


def _grouping(name: str, members: list[str]) -> dict:
    return {
        "name": name,
        "membership_criteria": [
            {
                "criteria_semantics": "NECESSARY",
                "logic": {
                    "operator": "OR",
                    "operands": [
                        {
                            "criterion_predicate": "HAS_MOLECULAR_FUNCTION",
                            "molecular_functions": [
                                {"term": {"id": root, "label": root}}
                            ],
                        }
                        for root in ROOTS
                    ],
                },
            }
        ],
        "members": [{"member": m, "member_type": "DISEASE"} for m in members],
    }


def _gene(hgnc: str, symbol: str, relationship: str | None = "CAUSATIVE") -> dict:
    rec = {"name": symbol, "gene_term": {"term": {"id": hgnc, "label": symbol}}}
    if relationship is not None:
        rec["relationship_type"] = relationship
    return rec


def _setup(
    tmp_path,
    monkeypatch,
    diseases: dict[str, list[dict]],
    annotations: dict[str, list[audit.Annotation]],
    *,
    uniprot: dict[str, str],
    review: dict[str, list[str]] | None = None,
    under_roots: set[str] | None = None,
):
    gdir = tmp_path / "groupings"
    ddir = tmp_path / "disorders"
    _write_yaml(gdir / "G.yaml", _grouping("G", list(diseases)))
    for name, genetic in diseases.items():
        _write_yaml(ddir / f"{name}.yaml", {"name": name, "genetic": genetic})
    monkeypatch.setattr(audit, "GROUPINGS_DIR", str(gdir))
    monkeypatch.setattr(audit, "DISORDERS_DIR", str(ddir))
    monkeypatch.setattr(audit, "hgnc_uniprot_index", lambda: dict(uniprot))
    monkeypatch.setattr(audit, "uniprot_for_hgnc", lambda hgnc, *, pause: (None, False))
    monkeypatch.setattr(
        audit,
        "fetch_annotations",
        lambda accs, roots, *, pause: {a: annotations.get(a, []) for a in accs},
    )
    monkeypatch.setattr(audit, "review_mf_terms", lambda: dict(review or {}))
    monkeypatch.setattr(
        audit,
        "terms_under_roots",
        lambda terms, roots, *, pause: {t for t in terms if t in (under_roots or set())},
    )
    (verdict,) = audit.build_verdicts(pause=0)
    return verdict


def _member(verdict: audit.GroupingVerdict, name: str) -> audit.MemberVerdict:
    return next(m for m in verdict.members if m.disease == name)


def test_roots_are_read_from_every_molecular_function_leaf():
    assert audit.molecular_function_roots(_grouping("G", [])) == ROOTS


def test_grouping_without_a_molecular_function_criterion_is_skipped(tmp_path, monkeypatch):
    gdir = tmp_path / "groupings"
    _write_yaml(gdir / "P.yaml", {"name": "P", "members": [{"member": "A"}]})
    monkeypatch.setattr(audit, "GROUPINGS_DIR", str(gdir))
    monkeypatch.setattr(audit, "DISORDERS_DIR", str(tmp_path / "disorders"))
    assert audit.build_verdicts(pause=0) == []


def test_experimental_annotation_supports_the_member(tmp_path, monkeypatch):
    v = _setup(
        tmp_path, monkeypatch,
        {"Alpha": [_gene("hgnc:1", "CHAN1")]},
        {"P00001": [audit.Annotation("GO:0005248", "IEA", False),
                    audit.Annotation("GO:0005248", "IDA", False)]},
        uniprot={"hgnc:1": "P00001"},
    )
    member = _member(v, "Alpha")
    assert member.verdict == "SUPPORTED"
    assert member.genes[0].verdict == "EXPERIMENTAL"
    assert member.genes[0].go_ids == ["GO:0005248"]


def test_evidence_classes_rank_strongest_first():
    gene = audit.GeneVerdict("hgnc:1", "X", "P1", annotations=[
        audit.Annotation("GO:1", "IEA", False),
        audit.Annotation("GO:1", "IBA", False),
    ])
    assert gene.verdict == "PHYLOGENETIC"
    gene.annotations.append(audit.Annotation("GO:1", "TAS", False))
    assert gene.verdict == "PHYLOGENETIC"
    gene.annotations = [audit.Annotation("GO:1", "IEA", False)]
    assert gene.verdict == "ELECTRONIC"


def test_not_annotation_never_supports(tmp_path, monkeypatch):
    v = _setup(
        tmp_path, monkeypatch,
        {"Beta": [_gene("hgnc:2", "PUMP1")]},
        {"P00002": [audit.Annotation("GO:0005216", "IDA", True)]},
        uniprot={"hgnc:2": "P00002"},
    )
    member = _member(v, "Beta")
    assert member.verdict == "UNSUPPORTED"
    assert member.genes[0].verdict == "NONE"
    assert [a.go_id for a in member.genes[0].negated] == ["GO:0005216"]


def test_unset_relationship_counts_as_causal(tmp_path, monkeypatch):
    v = _setup(
        tmp_path, monkeypatch,
        {"Gamma": [_gene("hgnc:3", "CHAN3", relationship=None)]},
        {"P00003": [audit.Annotation("GO:0005244", "IBA", False)]},
        uniprot={"hgnc:3": "P00003"},
    )
    assert _member(v, "Gamma").verdict == "SUPPORTED"


def test_disputed_only_member_is_no_causal_gene_but_its_gene_is_listed(tmp_path, monkeypatch):
    v = _setup(
        tmp_path, monkeypatch,
        {"Delta": [_gene("hgnc:4", "CHAN4", relationship="DISPUTED")]},
        {"P00004": [audit.Annotation("GO:0005248", "IDA", False)]},
        uniprot={"hgnc:4": "P00004"},
    )
    member = _member(v, "Delta")
    assert member.verdict == "NO_CAUSAL_GENE"
    assert [(g.symbol, g.relationship, g.verdict) for g in member.genes] == [
        ("CHAN4", "DISPUTED", "EXPERIMENTAL")
    ]


def test_non_causal_genes_are_dropped_when_a_causal_gene_exists(tmp_path, monkeypatch):
    v = _setup(
        tmp_path, monkeypatch,
        {"Eps": [_gene("hgnc:5", "CHAN5"), _gene("hgnc:6", "MOD6", relationship="MODIFIER")]},
        {"P00005": [audit.Annotation("GO:0005248", "IDA", False)]},
        uniprot={"hgnc:5": "P00005", "hgnc:6": "P00006"},
    )
    assert [g.symbol for g in _member(v, "Eps").genes] == ["CHAN5"]


def test_one_supported_gene_carries_a_multigene_member(tmp_path, monkeypatch):
    v = _setup(
        tmp_path, monkeypatch,
        {"Zeta": [_gene("hgnc:7", "CHAN7"), _gene("hgnc:8", "ENZ8")]},
        {"P00007": [audit.Annotation("GO:0005248", "IMP", False)]},
        uniprot={"hgnc:7": "P00007", "hgnc:8": "P00008"},
    )
    member = _member(v, "Zeta")
    assert member.verdict == "SUPPORTED"
    assert {g.symbol: g.verdict for g in member.genes} == {"CHAN7": "EXPERIMENTAL", "ENZ8": "NONE"}


def test_gene_without_uniprot_leaves_the_member_unresolved(tmp_path, monkeypatch):
    v = _setup(
        tmp_path, monkeypatch,
        {"Eta": [_gene("hgnc:9", "ORPHAN9")]},
        {},
        uniprot={},
    )
    member = _member(v, "Eta")
    assert member.verdict == "UNRESOLVED"
    assert member.genes[0].verdict == "NO_UNIPROT"


def test_gene_review_core_function_supports_a_gene_go_does_not_annotate(tmp_path, monkeypatch):
    v = _setup(
        tmp_path, monkeypatch,
        {"Theta": [_gene("hgnc:10", "REG10")]},
        {},
        uniprot={"hgnc:10": "P00010"},
        review={"hgnc:10": ["GO:0005246", "GO:0140314"]},
        under_roots={"GO:0005246"},
    )
    member = _member(v, "Theta")
    gene = member.genes[0]
    assert gene.review_terms == ["GO:0005246"]
    assert gene.verdict == "GENE_REVIEW"
    assert not gene.go_supported
    assert member.verdict == "SUPPORTED"


def test_go_evidence_outranks_the_gene_review_but_iea_does_not():
    gene = audit.GeneVerdict("hgnc:1", "X", "P1", review_terms=["GO:0005246"], annotations=[
        audit.Annotation("GO:0005248", "IEA", False),
    ])
    assert gene.verdict == "GENE_REVIEW"
    gene.annotations.append(audit.Annotation("GO:0005248", "IBA", False))
    assert gene.verdict == "PHYLOGENETIC"


def test_gene_review_stands_when_the_go_lookup_fails():
    gene = audit.GeneVerdict("hgnc:1", "X", None, lookup_failed=True, review_terms=["GO:0005246"])
    assert gene.verdict == "GENE_REVIEW"
    gene.review_terms = []
    assert gene.verdict == "LOOKUP_FAILED"


def test_failed_annotation_lookup_is_unresolved_not_unsupported(tmp_path, monkeypatch):
    gdir = tmp_path / "groupings"
    ddir = tmp_path / "disorders"
    _write_yaml(gdir / "G.yaml", _grouping("G", ["Iota"]))
    _write_yaml(ddir / "Iota.yaml", {"name": "Iota", "genetic": [_gene("hgnc:11", "CHAN11")]})
    monkeypatch.setattr(audit, "GROUPINGS_DIR", str(gdir))
    monkeypatch.setattr(audit, "DISORDERS_DIR", str(ddir))
    monkeypatch.setattr(audit, "hgnc_uniprot_index", lambda: {"hgnc:11": "P00011"})
    monkeypatch.setattr(audit, "fetch_annotations", lambda accs, roots, *, pause: None)
    monkeypatch.setattr(audit, "review_mf_terms", dict)
    (v,) = audit.build_verdicts(pause=0)
    assert _member(v, "Iota").verdict == "UNRESOLVED"


def test_strict_exits_one_only_on_unsupported(tmp_path, monkeypatch, capsys):
    _setup(
        tmp_path, monkeypatch,
        {"Kappa": [_gene("hgnc:12", "PUMP12")]},
        {},
        uniprot={"hgnc:12": "P00012"},
    )
    assert audit.main(["--strict"]) == 1
    assert audit.main([]) == 0
    assert "Kappa" in capsys.readouterr().out


def test_subtype_row_is_scoped_to_the_genes_it_names(tmp_path, monkeypatch):
    gdir = tmp_path / "groupings"
    ddir = tmp_path / "disorders"
    grouping = _grouping("G", [])
    grouping["members"] = [
        {
            "member": "Parent",
            "member_type": "SUBTYPE",
            "display_name": "Type A",
            "differentiating_mechanisms": [
                {"description": "A", "gene": {"term": {"id": "hgnc:20", "label": "ENZ20"}}}
            ],
        },
        {"member": "Parent", "member_type": "SUBTYPE", "display_name": "Type B"},
    ]
    _write_yaml(gdir / "G.yaml", grouping)
    # The parent's other subtype carries a channel gene; it must not rescue Type A.
    _write_yaml(ddir / "Parent.yaml", {"name": "Parent", "genetic": [
        _gene("hgnc:20", "ENZ20"), _gene("hgnc:21", "CHAN21"),
    ]})
    monkeypatch.setattr(audit, "GROUPINGS_DIR", str(gdir))
    monkeypatch.setattr(audit, "DISORDERS_DIR", str(ddir))
    monkeypatch.setattr(audit, "hgnc_uniprot_index", lambda: {"hgnc:20": "P00020", "hgnc:21": "P00021"})
    monkeypatch.setattr(
        audit, "fetch_annotations",
        lambda accs, roots, *, pause: {
            a: ([audit.Annotation("GO:0005248", "IDA", False)] if a == "P00021" else [])
            for a in accs
        },
    )
    monkeypatch.setattr(audit, "review_mf_terms", dict)
    (v,) = audit.build_verdicts(pause=0)
    by_label = {m.label: m for m in v.members}
    assert set(by_label) == {"Parent [subtype: Type A]", "Parent [subtype: Type B]"}
    type_a = by_label["Parent [subtype: Type A]"]
    assert [g.symbol for g in type_a.genes] == ["ENZ20"]
    assert type_a.verdict == "UNSUPPORTED"
    assert by_label["Parent [subtype: Type B]"].verdict == "SUBTYPE_UNSCOPED"


def test_failed_uniprot_fallback_is_lookup_failed_not_no_uniprot(tmp_path, monkeypatch):
    gdir = tmp_path / "groupings"
    ddir = tmp_path / "disorders"
    _write_yaml(gdir / "G.yaml", _grouping("G", ["Lambda"]))
    _write_yaml(ddir / "Lambda.yaml", {"name": "Lambda", "genetic": [_gene("hgnc:30", "CHAN30")]})
    monkeypatch.setattr(audit, "GROUPINGS_DIR", str(gdir))
    monkeypatch.setattr(audit, "DISORDERS_DIR", str(ddir))
    monkeypatch.setattr(audit, "hgnc_uniprot_index", dict)
    monkeypatch.setattr(audit, "uniprot_for_hgnc", lambda hgnc, *, pause: (None, True))
    monkeypatch.setattr(audit, "fetch_annotations", lambda accs, roots, *, pause: {})
    monkeypatch.setattr(audit, "review_mf_terms", dict)
    (v,) = audit.build_verdicts(pause=0)
    member = _member(v, "Lambda")
    assert member.genes[0].verdict == "LOOKUP_FAILED"
    assert member.verdict == "UNRESOLVED"


def test_failed_review_ancestor_lookup_is_flagged(tmp_path, monkeypatch):
    gdir = tmp_path / "groupings"
    ddir = tmp_path / "disorders"
    _write_yaml(gdir / "G.yaml", _grouping("G", ["Mu"]))
    _write_yaml(ddir / "Mu.yaml", {"name": "Mu", "genetic": [_gene("hgnc:40", "REG40")]})
    monkeypatch.setattr(audit, "GROUPINGS_DIR", str(gdir))
    monkeypatch.setattr(audit, "DISORDERS_DIR", str(ddir))
    monkeypatch.setattr(audit, "hgnc_uniprot_index", lambda: {"hgnc:40": "P00040"})
    monkeypatch.setattr(audit, "fetch_annotations", lambda accs, roots, *, pause: {})
    monkeypatch.setattr(audit, "review_mf_terms", lambda: {"hgnc:40": ["GO:0005246"]})
    monkeypatch.setattr(audit, "terms_under_roots", lambda terms, roots, *, pause: None)
    (v,) = audit.build_verdicts(pause=0)
    assert v.review_lookup_failed is True
    assert _member(v, "Mu").genes[0].review_terms == []


def test_failed_review_lookup_leaves_a_review_only_gene_unresolved(tmp_path, monkeypatch):
    gdir = tmp_path / "groupings"
    ddir = tmp_path / "disorders"
    _write_yaml(gdir / "G.yaml", _grouping("G", ["Nu", "Xi"]))
    _write_yaml(ddir / "Nu.yaml", {"name": "Nu", "genetic": [_gene("hgnc:50", "REG50")]})
    _write_yaml(ddir / "Xi.yaml", {"name": "Xi", "genetic": [_gene("hgnc:51", "CHAN51")]})
    monkeypatch.setattr(audit, "GROUPINGS_DIR", str(gdir))
    monkeypatch.setattr(audit, "DISORDERS_DIR", str(ddir))
    monkeypatch.setattr(audit, "hgnc_uniprot_index", lambda: {"hgnc:50": "P00050", "hgnc:51": "P00051"})
    monkeypatch.setattr(
        audit, "fetch_annotations",
        lambda accs, roots, *, pause: {
            a: ([audit.Annotation("GO:0005248", "IDA", False)] if a == "P00051" else [])
            for a in accs
        },
    )
    monkeypatch.setattr(
        audit, "review_mf_terms",
        lambda: {"hgnc:50": ["GO:0005246"], "hgnc:51": ["GO:0005248"]},
    )
    monkeypatch.setattr(audit, "terms_under_roots", lambda terms, roots, *, pause: None)
    (v,) = audit.build_verdicts(pause=0)
    review_only = _member(v, "Nu")
    assert review_only.genes[0].verdict == "LOOKUP_FAILED"
    assert review_only.verdict == "UNRESOLVED"
    # A gene GO already supports is unaffected by the failed review lookup.
    assert _member(v, "Xi").genes[0].verdict == "EXPERIMENTAL"
    assert _member(v, "Xi").verdict == "SUPPORTED"
