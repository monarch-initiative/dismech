# Disclaimer

This page is the canonical, long-form statement behind the short disclaimer shown at
the top of every generated DisMech page. The banner wording lives in
`src/dismech/templates/_disclaimer.html.j2`; keep the two in step when either changes.

## DisMech is AI-curated and AI-maintained

DisMech is **agent-forward**: the great majority of its content is generated and
maintained by AI curation agents, initiated either by human maintainers or by scheduled
GitHub Actions workflows. Human review is the pull-request gate, not a line-by-line
re-derivation of every assertion.

Concretely, this means:

- The prose descriptions, pathophysiology graphs, phenotype and treatment annotations,
  ontology term bindings, and evidence selections on a DisMech page were, in most cases,
  authored by an AI agent.
- Automated validation checks a great deal — that every cited reference exists, that
  every quoted snippet is an exact substring of the cited source, and that every ontology
  term identifier and label matches the authoritative ontology. These checks are strong
  protection against fabricated citations and invented ontology terms.
- They are **not** a guarantee of scientific correctness. A claim can cite a real paper,
  quote it accurately, and still be an incorrect or oversimplified reading of the
  underlying biology, or be attached to the wrong disease entity.

The curation process and its governance are described in
[Design Decisions §7](explanation/design-decisions.md) and in
[CONTRIBUTING.md](https://github.com/monarch-initiative/dismech/blob/main/CONTRIBUTING.md);
the evidence policy is [§6](explanation/design-decisions.md).

## DisMech is not medical advice

Beyond its AI-generated nature, the contents of this resource are **not intended to inform
medical diagnosis or treatment**. The inclusion of any statement, mechanism, phenotype,
drug, or clinical approach in a DisMech page is purely the result of generative methods and
human review applied to publicly accessible literature, data, and other curated biomedical
knowledge resources.

In particular:

- Nothing in DisMech should be used to diagnose a condition, select or dose a treatment,
  interpret a laboratory result, or make any other clinical decision.
- The presence of a treatment on a disease page is a record of what the cited literature
  describes. It is **not** a recommendation, an endorsement, or a statement about the
  treatment's safety, efficacy, availability, or regulatory approval status for any person.
- Reference ranges, prevalence figures, phenotype frequencies, and severity bands are
  curated from published sources of varying quality and populations. They are not
  calibrated for, and must not be applied to, any individual.
- DisMech is a *research* resource: its intended users are researchers, curators,
  ontologists, and developers of downstream computational tools.

**If you have a health concern, consult a qualified healthcare professional.** Do not
disregard or delay professional medical advice because of something you read here.

## Content status

DisMech is in active pre-alpha development. Coverage is incomplete and uneven across
diseases, entries change frequently, and identifiers are not yet stable enough to cite as
a fixed release. See the [QC and compliance documentation](quality-control.md) for how
entry completeness is measured.

## Reporting a problem

Errors in DisMech content are expected and reports are welcome. Please
[open an issue](https://github.com/monarch-initiative/dismech/issues) describing the
disease entry and the claim in question. Every disease page links to its own source YAML
file on GitHub, which is the authoritative record of what the page displays.

## Licensing and attribution

DisMech content is released under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
and is provided **"as is", without warranty of any kind**, express or implied. DisMech is
developed as part of the [Monarch Initiative](https://monarchinitiative.org).
