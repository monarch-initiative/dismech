"""Plain-language tooltips for the ontology term pills on rendered pages.

A pill reading ``abnormal extracellular matrix organization GO:0030198`` only
says something to a reader who already knows the ontology it came from. Issue
#8310 asks for a hover tooltip that spells the annotation out: which ontology
the term belongs to, what relation the annotation asserts, and a sentence
stating the whole thing including any qualifiers.

This module owns that text. :func:`term_tooltip` takes a descriptor (the
dict shape used throughout the templates) plus a *role* key naming the slot
the descriptor was found in, and returns plain text for the pill's ``title``
attribute::

    Gene Ontology (GO)
    Relation: this pathophysiological event involves this biological process
    This pathophysiological event involves abnormal extracellular matrix
    organization (GO:0030198). GO:0030198 is a biological process from the
    Gene Ontology.

Adding a new pill to a template means adding a matching entry to
:data:`TERM_ROLES`; an unknown role key degrades to the ontology line alone
rather than raising, so a missed entry never breaks a page build.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Ontology:
    """How one ontology is named in a tooltip.

    ``definite`` says whether the name takes a definite article: "from **the**
    Gene Ontology", but "from Mouse Genome Informatics". It is data rather than
    a rule inferred from the spelling, so a new entry cannot silently pick the
    wrong one.
    """

    prefix: str
    name: str
    definite: bool = True


#: Ontology prefixes to their naming record. Keyed by the upper-cased prefix so
#: lookups survive the repo's mixed CURIE casing (`hgnc:746` and `HGNC:746` both
#: resolve; see "CURIE Prefix Casing" in CLAUDE.md). Covers every prefix the
#: schema binds terms from, plus a handful of OBO prefixes that turn up in prose
#: and mappings.
ONTOLOGY_NAMES: dict[str, Ontology] = {
    "BFO": Ontology("BFO", "Basic Formal Ontology"),
    "CHEBI": Ontology("CHEBI", "Chemical Entities of Biological Interest", definite=False),
    "CL": Ontology("CL", "Cell Ontology"),
    "DOID": Ontology("DOID", "Human Disease Ontology"),
    "ECO": Ontology("ECO", "Evidence and Conclusion Ontology"),
    "ECTO": Ontology("ECTO", "Environmental Conditions, Treatments and Exposures Ontology"),
    "ENVO": Ontology("ENVO", "Environment Ontology"),
    "EXO": Ontology("ExO", "Exposure Ontology"),
    "FOODON": Ontology("FOODON", "FoodOn Food Ontology"),
    "GENO": Ontology("GENO", "Genotype Ontology"),
    "GO": Ontology("GO", "Gene Ontology"),
    "HGNC": Ontology("hgnc", "HUGO Gene Nomenclature Committee"),
    "HP": Ontology("HP", "Human Phenotype Ontology"),
    "ICD10CM": Ontology("ICD10CM", "ICD-10 Clinical Modification", definite=False),
    "ICD11F": Ontology("icd11f", "ICD-11 Foundation"),
    "LOINC": Ontology("LOINC", "Logical Observation Identifiers Names and Codes", definite=False),
    "MGI": Ontology("MGI", "Mouse Genome Informatics", definite=False),
    "MONDO": Ontology("MONDO", "Mondo Disease Ontology"),
    "MP": Ontology("MP", "Mammalian Phenotype Ontology"),
    "NCBITAXON": Ontology("NCBITaxon", "NCBI Taxonomy"),
    "NCIT": Ontology("NCIT", "NCI Thesaurus"),
    "OBA": Ontology("OBA", "Ontology of Biological Attributes"),
    "OBI": Ontology("OBI", "Ontology for Biomedical Investigations"),
    "OPL": Ontology("OPL", "Ontology for Parasite Lifecycle"),
    "PATO": Ontology("PATO", "Phenotype And Trait Ontology"),
    "PR": Ontology("PR", "Protein Ontology"),
    "RO": Ontology("RO", "Relation Ontology"),
    "SO": Ontology("SO", "Sequence Ontology"),
    "UBERON": Ontology("UBERON", "Uberon multi-species anatomy ontology"),
    "UPHENO": Ontology("UPHENO", "Unified Phenotype Ontology"),
    "XCO": Ontology("XCO", "Experimental Conditions Ontology"),
}


@dataclass(frozen=True)
class TermRole:
    """What a pill in a given template slot is asserting.

    ``subject`` is the annotated entity, written as it would start a sentence
    ("This pathophysiological event"); ``relation`` is the verb phrase linking
    it to the term ("involves"); ``kind`` names what sort of thing the term is
    ("biological process").
    """

    subject: str
    relation: str
    kind: str


#: Template slot -> what the pill in that slot means. Keys are
#: ``<container>.<slot>``, matching the ``role=`` argument passed from the
#: Jinja templates.
TERM_ROLES: dict[str, TermRole] = {
    # Pathophysiological events
    "pathophysiology.cell_types": TermRole(
        "This pathophysiological event", "involves", "cell type"
    ),
    "pathophysiology.gene": TermRole("This pathophysiological event", "involves", "gene"),
    "pathophysiology.protein_complexes": TermRole(
        "This pathophysiological event", "involves", "protein complex"
    ),
    "pathophysiology.biological_processes": TermRole(
        "This pathophysiological event", "involves", "biological process"
    ),
    "pathophysiology.molecular_functions": TermRole(
        "This pathophysiological event", "involves", "molecular function"
    ),
    "pathophysiology.cellular_components": TermRole(
        "This pathophysiological event", "involves", "cellular component"
    ),
    "pathophysiology.locations": TermRole(
        "This pathophysiological event", "occurs in", "anatomical location"
    ),
    # Rendered only on comorbidity pages today, where a shared-mechanism
    # hypothesis carries its own pathophysiology nodes.
    "pathophysiology.gene_products": TermRole(
        "This pathophysiological event", "involves", "gene product"
    ),
    # Genetic context
    "genetic_context.gene": TermRole("This genetic context", "concerns", "gene"),
    # Experimental models
    "model.organism": TermRole("This experimental model", "is built in", "organism"),
    "model.tissue_term": TermRole("This experimental model", "uses", "anatomical location"),
    "model.cell_types": TermRole("This experimental model", "uses", "cell type"),
    "model.genes": TermRole("This experimental model", "concerns", "gene"),
    # Perturbations applied within an experimental model
    "perturbation.gene": TermRole("This perturbation", "targets", "gene"),
    "perturbation.chemical_entities": TermRole("This perturbation", "uses", "chemical entity"),
    "perturbation.treatment_term": TermRole(
        "This perturbation", "applies", "clinical intervention"
    ),
    "perturbation.exposure_term": TermRole("This perturbation", "applies", "exposure"),
    "perturbation.triggers": TermRole("This perturbation", "is triggered by", "exposure"),
    "perturbation.biological_processes": TermRole(
        "This perturbation", "acts on", "biological process"
    ),
    # Readouts measured from an experimental model
    "readout.phenotype_term": TermRole("This readout", "measures", "phenotype"),
    "readout.biomarker_term": TermRole("This readout", "measures", "biomarker"),
    "readout.biological_processes": TermRole("This readout", "reports on", "biological process"),
    "readout.assays": TermRole("This readout", "is measured by", "assay"),
    # Experiments
    "experiment.experiment_type": TermRole("This experiment", "is of type", "experiment type"),
    "experiment.assays": TermRole("This experiment", "uses", "assay"),
    # Treatments and regimens
    "treatment.treatment_term": TermRole("This treatment", "is", "clinical intervention"),
    "treatment.location": TermRole("This treatment", "is delivered to", "anatomical location"),
    "regimen.treatment_term": TermRole("This regimen component", "is", "clinical intervention"),
    "regimen.location": TermRole(
        "This regimen component", "is delivered to", "anatomical location"
    ),
    # "chemical entity" would be wrong for most of these: CLAUDE.md routes NCIT
    # drug classes and biologics here alongside CHEBI small molecules, and a
    # monoclonal antibody is not a chemical entity (nor is a drug *class* an
    # entity at all). "therapeutic agent" covers both bindings without
    # over-claiming.
    "treatment.therapeutic_agent": TermRole("This treatment", "uses", "therapeutic agent"),
    "treatment.food": TermRole("This dietary modification", "concerns", "food"),
    "treatment.target_phenotype": TermRole("This treatment", "targets", "phenotype"),
    # Environmental factors
    "environment.exposure_term": TermRole("This environmental factor", "is", "exposure"),
    "environment.environment_context": TermRole(
        "This environmental factor", "occurs in", "environment"
    ),
    "environment.food_source": TermRole("This environmental factor", "is carried by", "food"),
    # Phenotypes and other clinical annotations
    "phenotype.phenotype_term": TermRole("This clinical feature", "is", "phenotype"),
    "effect.affected_cell_types": TermRole("This effect", "acts on", "cell type"),
    "subtype.gene": TermRole("This subtype", "is caused by variation in", "gene"),
    "variant.gene": TermRole("This variant", "is in", "gene"),
    "gene.gene_term": TermRole("This disease-associated gene", "is", "gene"),
    "trial.target_phenotypes": TermRole("This clinical trial", "targets", "phenotype"),
    # Comorbidities
    "comorbidity.phenotypes": TermRole("This comorbidity", "shares", "phenotype"),
    # A GO enrichment result may be a process, a function or a component, so the
    # noun stays at "term" rather than claiming one of the three.
    "signal.go_enrichment": TermRole("This association signal", "is enriched for", "term"),
    # Datasets
    # Sample types bind a tissue far more often than a cell type (UBERON 76,
    # CL 15), so "cell type" would misdescribe most of them.
    "dataset.sample_types": TermRole("This dataset", "samples", "sample type"),
    "dataset.exposures": TermRole("This dataset", "covers", "exposure"),
    # Shared mechanism modules
    "module.cell_types": TermRole("This mechanism module", "involves", "cell type"),
    "module.biological_processes": TermRole(
        "This mechanism module", "involves", "biological process"
    ),
}

#: Modifier values that read as an adjective in front of the term, so they can be
#: folded into the sentence ("involves decreased insulin secretion"). The rest of
#: ModifierEnum -- the qualitative GAIN_OF_FUNCTION / LOSS_OF_FUNCTION pair that
#: CLAUDE.md separates from these quantitative values -- are noun phrases, and
#: "involves gain of function phosphatase activity" is not a sentence, so they
#: trail in the qualifier clause instead.
_ADJECTIVAL_MODIFIERS = frozenset(
    {"INCREASED", "DECREASED", "ABNORMAL", "DYSREGULATED", "ABSENT"}
)

#: Every Descriptor slot the tooltip reports as a qualifier. Named once so a
#: descriptor can be recomposed without silently dropping any of them.
_QUALIFIER_SLOTS = frozenset(
    {
        "modifier",
        "laterality",
        "spatial_extent",
        "temporality",
        "clinical_course",
        "severity",
        "located_in",
        "onset",
        "qualifiers",
    }
)

#: Descriptor qualifier slots that carry a plain scalar value, in the order they
#: read most naturally in a sentence. `modifier` is handled separately because
#: an adjectival one reads as part of the term itself ("decreased insulin
#: secretion").
_SCALAR_QUALIFIER_SLOTS: tuple[tuple[str, str], ...] = (
    ("laterality", "laterality"),
    ("spatial_extent", "extent"),
    ("temporality", "temporality"),
    ("clinical_course", "course"),
    ("severity", "severity"),
)


def _humanize(value: Any) -> str:
    """Render an enum-ish value the way the pills do: lower case, spaces."""
    text = str(value or "").strip()
    return text.replace("_", " ").lower()


def _as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def curie_prefix(curie: str | None) -> str:
    """Upper-cased prefix of a CURIE, or "" when there isn't one."""
    if not curie or ":" not in str(curie):
        return ""
    return str(curie).split(":", 1)[0].strip().upper()


def ontology_label(curie: str | None) -> str:
    """Full ontology name for a CURIE, e.g. ``CL:0000115`` -> "Cell Ontology".

    Returns "" for CURIEs from prefixes that are not ontologies (PMIDs, dataset
    accessions) or that aren't in :data:`ONTOLOGY_NAMES`.
    """
    known = ONTOLOGY_NAMES.get(curie_prefix(curie))
    return known.name if known else ""


def _ontology_heading(curie: str | None) -> str:
    """First tooltip line: ``Cell Ontology (CL)``."""
    known = ONTOLOGY_NAMES.get(curie_prefix(curie))
    if not known:
        return ""
    return f"{known.name} ({known.prefix})"


def _article(noun: str) -> str:
    return "an" if noun[:1].lower() in "aeiou" else "a"


def _descriptor_label(descriptor: Any) -> str:
    """Readable label for a nested Descriptor, or "" if it has none.

    Several slots -- ``located_in``, and both sides of a legacy ``Qualifier`` --
    range over a whole Descriptor rather than a scalar. Formatting one directly
    interpolates its dict repr, so every such slot resolves through here.
    """
    descriptor_map = _as_mapping(descriptor)
    if not descriptor_map:
        return ""
    term = _as_mapping(descriptor_map.get("term"))
    label = (
        descriptor_map.get("preferred_term")
        or term.get("label")
        or descriptor_map.get("name")
        or term.get("id")
    )
    return str(label).strip() if label else ""


def _onset_phrase(onset: Any) -> str:
    """Condense an OnsetDescriptor into one qualifier phrase."""
    onset_map = _as_mapping(onset)
    if not onset_map:
        return ""
    ages = []
    mean_age = onset_map.get("mean_age_years")
    min_age = onset_map.get("min_age_years")
    max_age = onset_map.get("max_age_years")
    if mean_age is not None:
        ages.append(f"mean {mean_age}y")
    if min_age is not None and max_age is not None:
        ages.append(f"range {min_age}-{max_age}y")
    elif min_age is not None:
        ages.append(f"from {min_age}y")
    elif max_age is not None:
        ages.append(f"up to {max_age}y")

    # The category is an adjective, so it reads as "infantile onset" rather than
    # the stiffer "onset infantile" the qualifier clause used to produce.
    category = _humanize(onset_map.get("onset_category"))
    if not category:
        lead = "onset"
    elif category.endswith("onset"):
        # No OnsetEnum value ends this way today; the guard keeps a future one
        # from reading "adult onset onset".
        lead = category
    else:
        lead = f"{category} onset"
    if not category and not ages:
        return ""
    return f"{lead}, {', '.join(ages)}" if ages else lead


def _qualifier_phrases(descriptor: Mapping[str, Any]) -> list[str]:
    """Every qualifier on a descriptor, as short ``key value`` phrases."""
    phrases = []

    # A non-adjectival modifier cannot be folded into the sentence, so it leads
    # the qualifier clause: "..., qualified as gain of function".
    modifier = descriptor.get("modifier")
    if modifier and str(modifier).strip().upper() not in _ADJECTIVAL_MODIFIERS:
        phrases.append(_humanize(modifier))

    for slot, wording in _SCALAR_QUALIFIER_SLOTS:
        value = descriptor.get(slot)
        if value:
            phrases.append(f"{wording} {_humanize(value)}")

    located_in = _descriptor_label(descriptor.get("located_in"))
    if located_in:
        phrases.append(f"located in {located_in}")

    onset = _onset_phrase(descriptor.get("onset"))
    if onset:
        phrases.append(onset)

    # `qualifiers` is deprecated in favour of the explicit slots above, but
    # legacy entries still carry predicate/value pairs worth showing. Both sides
    # range over Descriptor, not over a scalar -- reading them as strings put a
    # Python dict repr in the title attribute.
    for qualifier in descriptor.get("qualifiers") or []:
        qualifier_map = _as_mapping(qualifier)
        predicate = _descriptor_label(qualifier_map.get("predicate"))
        value = _descriptor_label(qualifier_map.get("value"))
        if predicate and value:
            phrases.append(f"{predicate} {value}")

    return phrases


#: Where a `SampleTypeDescriptor` may hold its ontology binding, most telling
#: first. A sample is best described by the cell type when one was recorded:
#: "peripheral blood monocytes" is explained by `monocyte` (CL:0000576), not by
#: the `blood` (UBERON:0000178) sitting in the descriptor's own `term`. The
#: descriptor's own binding comes next -- it is sometimes a specimen term no
#: nested slot carries, e.g. `bronchoalveolar lavage` (NCIT:C13195) -- and the
#: tissue last, since it names where the sample came from rather than what it is.
#: Across kb/disorders these are rarely in tension: of 187 sample types, 92 carry
#: more than one binding but most repeat the same CURIE.
_SAMPLE_TYPE_BINDINGS = ("cell_type_term", "term", "tissue_term")


def sample_type_descriptor(sample_type: Any) -> Mapping[str, Any]:
    """Pair a dataset sample type's displayed label with its ontology binding.

    The pill always displays the outer ``preferred_term``, so the tooltip has to
    describe *that* label rather than whichever nested object happens to hold a
    CURIE -- otherwise the hover text names a different thing than the pill. The
    binding is chosen by :data:`_SAMPLE_TYPE_BINDINGS`, and the returned mapping
    drives both the tooltip and the identifier chip, so the two cannot disagree
    about which CURIE this pill is about.

    The outer label is kept in front of the chosen binding's own, which turns a
    difference between them into the ordinary "annotated with <label>" case
    rather than a silent substitution. Qualifiers written on the outer
    descriptor come across too -- no sample type in the KB carries one today,
    but the nested branch is the common path now, so dropping them would be a
    trap for whoever writes the first.
    """
    sample_map = _as_mapping(sample_type)
    if not sample_map:
        return {}

    for slot in _SAMPLE_TYPE_BINDINGS:
        binding = sample_map if slot == "term" else _as_mapping(sample_map.get(slot))
        if not _as_mapping(binding.get("term")).get("id"):
            continue
        if binding is sample_map:
            return sample_map
        outer = {
            key: value
            for key, value in sample_map.items()
            if key in _QUALIFIER_SLOTS and value
        }
        # Only override the label when the sample type has one of its own;
        # otherwise the binding's own preferred_term is the better one.
        if sample_map.get("preferred_term"):
            outer["preferred_term"] = sample_map["preferred_term"]
        return {**binding, **outer}

    return sample_map


def term_tooltip(descriptor: Any, role: str = "") -> str:
    """Build the hover text for one ontology term pill.

    ``descriptor`` is a descriptor mapping as the templates see it: an optional
    ``preferred_term``, an optional ``term`` with ``id``/``label``, and any
    qualifier slots. ``role`` is a key into :data:`TERM_ROLES` naming the slot
    the pill sits in. Returns "" when there is nothing worth saying, so callers
    can skip the ``title`` attribute entirely.
    """
    descriptor_map = _as_mapping(descriptor)
    if not descriptor_map:
        return ""

    # Module summary pages flatten a descriptor down to a bare {id, label}
    # pair before rendering, so accept the term fields at the top level too.
    term = _as_mapping(descriptor_map.get("term"))
    if not term and descriptor_map.get("id"):
        term = descriptor_map
    curie = str(term.get("id") or "").strip()
    term_label = str(term.get("label") or "").strip()
    preferred = str(descriptor_map.get("preferred_term") or "").strip()
    display = preferred or term_label or str(descriptor_map.get("name") or "").strip()
    if not display and not curie:
        return ""

    lines = []
    heading = _ontology_heading(curie)
    if heading:
        lines.append(heading)

    term_role = TERM_ROLES.get(role)
    if term_role:
        lines.append(
            f"Relation: {term_role.subject[:1].lower()}{term_role.subject[1:]} "
            f"{term_role.relation} this {term_role.kind}"
        )

        # An adjectival modifier reads as part of the annotated thing rather than
        # as a separate qualifier: "involves decreased insulin secretion".
        # Curators often bake it into the label already ("abnormal ..." with
        # modifier ABNORMAL), so only prepend it when it is not already there.
        raw_modifier = descriptor_map.get("modifier")
        modifier = (
            _humanize(raw_modifier)
            if str(raw_modifier or "").strip().upper() in _ADJECTIVAL_MODIFIERS
            else ""
        )
        subject_phrase = display
        if modifier and not display.lower().startswith(modifier):
            subject_phrase = f"{modifier} {display}"
        sentence = f"{term_role.subject} {term_role.relation} {subject_phrase}"
        if curie:
            # A preferred_term may be more specific than the ontology label
            # (see CLAUDE.md), so name both when they genuinely differ --
            # capitalisation alone is not a difference worth a clause.
            differs = preferred and term_label and preferred.casefold() != term_label.casefold()
            if differs:
                sentence += f", annotated with {term_label} ({curie})"
            else:
                sentence += f" ({curie})"
        qualifiers = _qualifier_phrases(descriptor_map)
        if qualifiers:
            sentence += f", qualified as {'; '.join(qualifiers)}"
        sentence += "."

        ontology = ONTOLOGY_NAMES.get(curie_prefix(curie))
        if curie and ontology:
            source = f"the {ontology.name}" if ontology.definite else ontology.name
            sentence += (
                f" {curie} is {_article(term_role.kind)} {term_role.kind} from {source}."
            )
        lines.append(sentence)

    return "\n".join(lines)
