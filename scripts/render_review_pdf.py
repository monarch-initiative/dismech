#!/usr/bin/env python3
"""Render a disorder YAML file to a clean PDF for expert review."""

import argparse
import re
import subprocess
import tempfile
import textwrap
from datetime import datetime
from pathlib import Path

import yaml
from jinja2 import Environment

TEMPLATE = r"""
# {{ d.name }}

> **Expert review report — Disorder Mechanisms Knowledge Base (dismech)**
> Generated from the curated disease record for **{{ d.name }}**
> ([dismech](https://github.com/monarch-initiative/dismech), commit `{{ commit_hash }}`).
> The contents are **highly experimental (pre-alpha)** and are presented to medical
> experts to verify the correctness, completeness, and clinical plausibility of the
> machine-assisted curation. Each factual claim is accompanied by its supporting
> literature, an exact quoted snippet, and an interpretation, so that statements can
> be checked against their source.

### How to read this report

The report follows a fixed 17-section structure (Identity → Provenance). Where a claim is
backed by literature you will see an **Evidence** block giving the reference
(PubMed/DOI/trial ID), whether the source **supports** or refutes the claim, the **type**
of evidence (human clinical, model organism, in vitro, etc.), an **exact quote** from the
source, and a short **interpretation**. Superscript numbers (e.g. ^1^) refer to the
**Glossary** in §17. Sections marked *Not curated for this disease* are part of the
standard template but currently hold no data for this entry — pointers are welcome.
Sections marked *Not yet modeled in the dismech schema* are gaps in the data model itself.
*Please flag anything wrong, overstated, out of date, or missing — especially in
**§6 Pathophysiology** and **§15 Open questions**, where expert judgement is most valuable.*

---

## 1. Identity

| | |
|---|---|
| **Disease** | {{ d.name }} |
{% if d.disease_term %}| **MONDO** | `{{ d.disease_term.term.id }}` — {{ d.disease_term.term.label }} |
{% endif %}{% set m = d.mappings %}{% if m and (m.mondo_mappings or m.icd10cm_mappings or m.icd11f_mappings or m.ncit_mappings) %}| **Cross-references** | {% if m.icd10cm_mappings %}ICD-10-CM: {{ m.icd10cm_mappings | map(attribute='id') | join(', ') }}. {% endif %}{% if m.icd11f_mappings %}ICD-11: {{ m.icd11f_mappings | map(attribute='id') | join(', ') }}. {% endif %}{% if m.ncit_mappings %}NCIT: {{ m.ncit_mappings | map(attribute='id') | join(', ') }}. {% endif %}{% if m.mondo_mappings %}MONDO: {{ m.mondo_mappings | map(attribute='id') | join(', ') }}.{% endif %} |
{% endif %}{% if d.synonyms %}| **Synonyms** | {{ d.synonyms | join('; ') }} |
{% endif %}{% if d.category %}| **Category** | {{ d.category }} |
{% endif %}{% if d.parents %}| **Parent classes** | {{ d.parents | join(' › ') }} |
{% endif %}{% if d.has_subtypes %}| **Subtypes captured** | {{ d.has_subtypes | length }} |
{% endif %}{% if d.phenotypes %}| **Phenotypes captured** | {{ d.phenotypes | length }} |
{% endif %}{% if d.genetic %}| **Genetic factors captured** | {{ d.genetic | length }} |
{% endif %}{% if d.treatments %}| **Treatments captured** | {{ d.treatments | length }} |
{% endif %}{% if d.creation_date %}| **Record created** | {{ d.creation_date }} |
{% endif %}

## 2. Overview

{{ d.description | wordwrap(90) }}

## 3. Epidemiology

{% if d.prevalence or d.epidemiology %}
{% if d.prevalence %}
**Prevalence / frequency:**
{% for p in d.prevalence %}
- {% if p.population %}{{ p.population }}: {% endif %}{{ p.percentage }}{% if p.subtype %} ({{ p.subtype }}){% endif %}{% if p.notes %} -- {{ p.notes }}{% endif %}
{% endfor %}
{% endif %}
{% if d.epidemiology %}
{% for ep in d.epidemiology | aslist %}
### {{ ep.name }}

{{ ep.description | default('', true) | wordwrap(90) }}
{% if ep.minimum_value is not none or ep.maximum_value is not none or ep.mean_range %}**Value:** {% if ep.mean_range %}{{ ep.mean_range }}{% else %}{% if ep.minimum_value is not none %}{{ ep.minimum_value }}{% endif %}{% if ep.minimum_value is not none and ep.maximum_value is not none %}–{% endif %}{% if ep.maximum_value is not none %}{{ ep.maximum_value }}{% endif %}{% endif %}{% if ep.unit %} {{ ep.unit }}{% endif %}

{% endif %}{% if ep.factors %}**Factors:** {{ ep.factors | join(', ') }}

{% endif %}{% if ep.notes %}*{{ ep.notes }}*
{% endif %}{{ evidence_block(ep.evidence, claim=ep.name + " for " + d.name) }}
{% endfor %}
{% endif %}
{% else %}*Not curated for this disease.*
{% endif %}

## 4. Classification

{% set cls = d.classifications %}
{% if not (cls and (cls.harrisons_chapter or cls.mechanistic_category or cls.iuis_category or cls.channelopathy_category or cls.lysosomal_storage_category or cls.icdo_morphology)) and not d.has_subtypes %}*Not curated for this disease.*
{% endif %}
{% if cls and (cls.harrisons_chapter or cls.mechanistic_category or cls.iuis_category or cls.channelopathy_category or cls.lysosomal_storage_category or cls.icdo_morphology) %}
### Nosological placement
{% if cls.harrisons_chapter %}
- *Harrison's chapter:* {{ cls_val(cls.harrisons_chapter) }}
{% endif %}{% if cls.mechanistic_category %}- *Mechanistic category:* {{ cls_val(cls.mechanistic_category) }}
{% endif %}{% if cls.iuis_category %}- *IUIS immunodeficiency category:* {{ cls_val(cls.iuis_category) }}
{% endif %}{% if cls.channelopathy_category %}- *Channelopathy category:* {{ cls_val(cls.channelopathy_category) }}
{% endif %}{% if cls.lysosomal_storage_category %}- *Lysosomal storage category:* {{ cls_val(cls.lysosomal_storage_category) }}
{% endif %}{% if cls.icdo_morphology %}- *ICD-O morphology:* {{ cls_val(cls.icdo_morphology) }}
{% endif %}
{% endif %}
{% if d.has_subtypes %}
### Subtypes
{% for s in d.has_subtypes %}
#### {{ s.name }}{% if s.classification %} ({{ s.classification }}){% endif %}

{{ s.description | wordwrap(90) }}
{{ evidence_block(s.evidence, claim=s.name + " is a subtype of " + d.name) }}
{% endfor %}
{% endif %}

## 5. Etiology

{% if not (d.genetic or d.inheritance or d.variants or d.environmental or d.infectious_agent) %}*Not curated for this disease.*
{% endif %}
{% if d.genetic or d.inheritance or d.variants %}
### Genetics
{% for g in d.genetic | aslist %}
#### {{ g.name }}
{% if g.association %}**Association:** {{ g.association }}{% endif %}

{% if g.gene_term %}
**Gene:** {{ g.gene_term.preferred_term }} -- `{{ g.gene_term.term.id }}` ({{ g.gene_term.term.label }})
{% endif %}

{% if g.features %}{{ g.features | wordwrap(90) }}{% endif %}

{% if g.inheritance %}
**Inheritance:**
{% for inh in g.inheritance %}
- {{ inh.name }}{% if inh.inheritance_term %} -- `{{ inh.inheritance_term.term.id }}`{% endif %}{% if inh.penetrance %} | Penetrance: {{ el(inh.penetrance) }}{% endif %}{% if inh.expressivity %} | Expressivity: {{ el(inh.expressivity) }}{% endif %}{% if inh.de_novo_rate %} | De novo rate: {{ inh.de_novo_rate }}{% endif %}

{{ evidence_block(inh.evidence, claim=d.name + " follows " + inh.name, indent=2) }}
{% endfor %}
{% endif %}

{% if g.variants %}
**Variants:**
{% for v in g.variants %}
##### {{ v.name }}
{% if v.clinical_significance %}**Clinical significance:** {{ el(v.clinical_significance) }}{% endif %}

{{ v.description | default('', true) | wordwrap(90) }}
{{ evidence_block(v.evidence, claim=v.name + " is a variant associated with " + d.name) }}
{% endfor %}
{% endif %}
{{ evidence_block(g.evidence, claim=g.name + " is a genetic basis of " + d.name) }}
{% endfor %}
{% if d.variants %}
**Disease-level variants:**
{% for v in d.variants %}
#### {{ v.name }}
{% if v.gene %}**Gene:** {{ v.gene.preferred_term | default(v.gene) }}{% endif %}{% if v.clinical_significance %} | **Clinical significance:** {{ el(v.clinical_significance) }}{% endif %}

{{ v.description | default('', true) | wordwrap(90) }}
{{ evidence_block(v.evidence, claim=v.name + " is a variant associated with " + d.name) }}
{% endfor %}
{% endif %}
{% if d.inheritance %}
### Inheritance (disease-level)
{% for inh in d.inheritance | aslist %}
#### {{ inh.name }}{% if inh.inheritance_term %} -- `{{ inh.inheritance_term.term.id }}`{% endif %}

{% if inh.penetrance %}**Penetrance:** {{ el(inh.penetrance) }}{% if inh.penetrance_percentage %} ({{ inh.penetrance_percentage }}%){% endif %}{% endif %}{% if inh.expressivity %} | **Expressivity:** {{ el(inh.expressivity) }}{% endif %}{% if inh.de_novo_rate %} | **De novo rate:** {{ inh.de_novo_rate }}{% endif %}{% if inh.parent_of_origin_effect %} | **Parent-of-origin effect**{% endif %}

{% if inh.description %}{{ inh.description | wordwrap(90) }}{% endif %}
{{ evidence_block(inh.evidence, claim=d.name + " follows " + inh.name) }}
{% endfor %}
{% endif %}
{% endif %}
{% if d.environmental %}
### Environmental factors
{% for e in d.environmental %}
#### {{ e.name }}
{% if e.presence %}**Presence:** {{ e.presence }}{% endif %}

{{ e.description | default('', true) | wordwrap(90) }}
{{ evidence_block(e.evidence, claim=e.name + " is an environmental factor in " + d.name) }}
{% endfor %}
{% endif %}
{% if d.infectious_agent %}
### Infectious agent
{% for ia in d.infectious_agent %}
#### {{ ia.name }}
{{ ia.description | default('', true) | wordwrap(90) }}
{{ evidence_block(ia.evidence, claim=ia.name + " is an infectious agent causing " + d.name) }}
{% endfor %}
{% endif %}

## 6. Pathophysiology

{% if not (d.mechanistic_hypotheses or d.pathophysiology) %}*Not curated for this disease.*
{% endif %}
{% if d.mechanistic_hypotheses %}
### Mechanistic models

*Overarching, falsifiable models the knowledge base uses to organise the mechanism of this
disease. These most need expert scrutiny: is the canonical model right, are the
alternatives credible, and is anything missing?*

{% for h in d.mechanistic_hypotheses %}
#### {{ h.hypothesis_label or h.hypothesis_group_id }}{% if h.status %} — *{{ el(h.status) }}*{% endif %}

{% if h.applies_to_subtypes %}**Applies to subtypes:** {{ h.applies_to_subtypes | join(', ') }}

{% endif %}{{ h.description | wordwrap(90) }}
{% if h.notes %}
*Curator notes:* {{ h.notes }}
{% endif %}
{{ evidence_block(h.evidence, claim=(h.hypothesis_label or h.hypothesis_group_id) + " is a proposed mechanistic model of " + d.name) }}
{% endfor %}
{% endif %}
{% if d.pathophysiology %}
### Pathway nodes

{% for p in d.pathophysiology %}
#### {{ p.name }}
{% if p.conforms_to %}
*Conforms to module:* `{{ p.conforms_to }}`
{% endif %}

{{ p.description | wordwrap(90) }}

{% if p.cell_types %}
**Cell types:**
{% for ct in p.cell_types %}
- {{ ct.preferred_term }} -- `{{ ct.term.id }}` ({{ ct.term.label }}){% if ct.modifier %} [{{ el(ct.modifier) }}]{% endif %}

{% endfor %}
{% endif %}
{% if p.biological_processes %}
**Biological processes:**
{% for bp in p.biological_processes %}
- {{ bp.preferred_term }} -- `{{ bp.term.id }}` ({{ bp.term.label }}){% if bp.modifier %} [{{ el(bp.modifier) }}]{% endif %}

{% endfor %}
{% endif %}
{% if p.molecular_functions %}
**Molecular functions:**
{% for mf in p.molecular_functions %}
- {{ mf.preferred_term }} -- `{{ mf.term.id }}` ({{ mf.term.label }}){% if mf.modifier %} [{{ el(mf.modifier) }}]{% endif %}

{% endfor %}
{% endif %}
{% if p.locations %}
**Anatomical locations:**
{% for loc in p.locations %}
- {{ loc.preferred_term }} -- `{{ loc.term.id }}` ({{ loc.term.label }})
{% endfor %}
{% endif %}
{% if p.cellular_components %}
**Cellular components:**
{% for cc in p.cellular_components %}
- {{ cc.preferred_term }} -- `{{ cc.term.id }}` ({{ cc.term.label }})
{% endfor %}
{% endif %}
{% if p.chemical_entities %}
**Chemical entities:**
{% for ce in p.chemical_entities %}
- {{ ce.preferred_term }} -- `{{ ce.term.id }}` ({{ ce.term.label }}){% if ce.modifier %} [{{ el(ce.modifier) }}]{% endif %}

{% endfor %}
{% endif %}
{% if p.gene_products %}
**Gene products:**
{% for gp in p.gene_products %}
- {{ gp.preferred_term }} -- `{{ gp.term.id }}` ({{ gp.term.label }})
{% endfor %}
{% endif %}
{% if p.triggers %}
**Triggers:**
{% for t in p.triggers %}
- {{ t.preferred_term }}{% if t.term %} -- `{{ t.term.id }}` ({{ t.term.label }}){% endif %}

{% endfor %}
{% endif %}
{% if p.downstream %}
**Leads to (downstream effects):**
{% for de in p.downstream %}
- **→ {{ de.target }}**{% if de.causal_link_type %} [{{ el(de.causal_link_type) }}]{% endif %}: {{ de.description }}
{% if de.intermediate_mechanisms %}  *(via: {{ de.intermediate_mechanisms | join('; ') }})*
{% endif %}{% if de.evidence %}{{ evidence_block(de.evidence, claim=p.name + " leads to " + de.target, indent=1) }}
{% endif %}{% endfor %}
{% endif %}
{% if p.notes %}
*Notes:* {{ p.notes }}
{% endif %}
{{ evidence_block(p.evidence, claim=p.name + " is a pathophysiological mechanism in " + d.name) }}
{% endfor %}
{% endif %}

## 7. Clinical features

{% if d.phenotypes %}
| Phenotype | HPO term | System | Frequency | Qualifiers | Evidence |
|---|---|---|---|---|---|
{% for ph in d.phenotypes %}| **{{ cell(ph.name) }}**{% if ph.subtype %} {{ cell('(' + ph.subtype + ')') }}{% endif %}{% if ph.description %}<br>{{ cell(ph.description) }}{% endif %} | {{ cell(pheno_hpo(ph)) }} | {{ cell(ph.category) }} | {% if ph.frequency %}{{ freq(ph.frequency) }}{% else %}—{% endif %} | {{ cell(pheno_quals(ph)) }} | {{ ev_cell(ph.evidence) }} |
{% endfor %}
{% else %}*Not curated for this disease.*
{% endif %}

## 8. Biomarkers

### Biochemical biomarkers
{% if d.biochemical %}
{% for b in d.biochemical %}
#### {{ b.name }}
{% if b.presence %}**Presence:** {{ b.presence }}{% endif %}{% if b.frequency %} | **Frequency:** {{ freq(b.frequency) }}{% endif %}

{{ b.description | default('', true) | wordwrap(90) }}
{% if b.biomarker_term %}
**Biomarker term:** {{ b.biomarker_term.preferred_term }} -- `{{ b.biomarker_term.term.id }}` ({{ b.biomarker_term.term.label }})
{% endif %}
{% if b.reference_ranges %}
{% for rr in b.reference_ranges %}
**Reference range{% if rr.population %} ({{ rr.population }}){% endif %}:** {% if rr.lower_bound is not none %}{{ rr.lower_bound }}{% else %}—{% endif %}–{% if rr.upper_bound is not none %}{{ rr.upper_bound }}{% else %}—{% endif %}{% if rr.unit %} {{ rr.unit }}{% endif %}{% if rr.loinc_term %} (LOINC `{{ rr.loinc_term.id }}`){% endif %}

{% if rr.interpretation_bands %}
{% for band in rr.interpretation_bands %}
- *{{ band.name }}*: {% if band.lower_bound is not none %}≥{{ band.lower_bound }}{% endif %}{% if band.lower_bound is not none and band.upper_bound is not none %} and {% endif %}{% if band.upper_bound is not none %}<{{ band.upper_bound }}{% endif %}{% if band.unit %} {{ band.unit }}{% endif %}{% if band.severity %} — {{ band.severity }}{% endif %}{% if band.interpretation %} ({{ band.interpretation }}){% endif %}
{% endfor %}
{% endif %}{% if rr.notes %}*{{ rr.notes }}*
{% endif %}{{ evidence_block(rr.evidence, claim="reference interval for " + b.name, indent=1) }}
{% endfor %}
{% endif %}
{{ evidence_block(b.evidence, claim=b.name + " is a biochemical marker of " + d.name) }}
{% endfor %}
{% else %}*Not curated for this disease.*
{% endif %}

### Digital biomarkers

*Not yet modeled in the dismech schema (e.g., wearable/sensor-derived,
accelerometry, or digital speech markers).*

## 9. Diagnosis

{% if not (d.diagnosis or d.definitions or d.histopathology or d.differential_diagnoses) %}*Not curated for this disease.*
{% endif %}
{% if d.diagnosis %}
### Diagnostic criteria
{% for dx in d.diagnosis %}
#### {{ dx.name }}
{{ dx.description | default('', true) | wordwrap(90) }}
{{ evidence_block(dx.evidence, claim=dx.name + " is a diagnostic criterion for " + d.name) }}
{% endfor %}
{% endif %}
{% if d.histopathology %}
### Investigations — histopathology
{% for h in d.histopathology %}
#### {{ h.name }}
{% if h.frequency %}**Frequency:** {{ freq(h.frequency) }}{% endif %}{% if h.diagnostic %} | **Diagnostic**{% endif %}

{{ h.description | default('', true) | wordwrap(90) }}
{% if h.finding_term %}
**Finding term:** {{ h.finding_term.preferred_term }} -- `{{ h.finding_term.term.id }}` ({{ h.finding_term.term.label }})
{% endif %}
{{ evidence_block(h.evidence, claim=h.name + " is a histopathological finding in " + d.name) }}
{% endfor %}
{% endif %}
{% if d.definitions %}
### Computable case definitions
{% for df in d.definitions %}
#### {{ df.name }}{% if df.definition_type %} ({{ df.definition_type }}){% endif %}

{{ df.description | default('', true) | wordwrap(90) }}
{% if df.scope %}**Scope:** {{ df.scope }}{% endif %}
{% if df.inclusion_criteria %}
**Inclusion criteria:**
{% for c in df.inclusion_criteria %}
- {{ c }}
{% endfor %}
{% endif %}{% if df.exclusion_criteria %}
**Exclusion criteria:**
{% for c in df.exclusion_criteria %}
- {{ c }}
{% endfor %}
{% endif %}{{ evidence_block(df.evidence, claim=df.name + " is a definition of " + d.name) }}
{% endfor %}
{% endif %}

{% if d.differential_diagnoses %}
### Differential diagnosis
{% for dd in d.differential_diagnoses %}
#### {{ dd.name }}
{{ dd.description | default('', true) | wordwrap(90) }}
{% if dd.distinguishing_features %}
**Distinguishing features:**
{% for f in dd.distinguishing_features %}
- {{ f }}
{% endfor %}
{% endif %}
{{ evidence_block(dd.evidence, claim=dd.name + " is a differential diagnosis for " + d.name) }}
{% endfor %}
{% endif %}

## 10. Natural history

{% if d.progression or d.stages %}
{% if d.progression %}
**Disease course:**
{% for p in d.progression %}
- {% if p.phase %}{{ p.phase }}: {% endif %}{% if p.duration %}Duration: {{ p.duration }}{% endif %}{% if p.notes %} -- {{ p.notes }}{% endif %}
{% endfor %}
{% endif %}
{% if d.stages %}
### Disease stages
{% for s in d.stages %}
#### {{ s.name }}
{{ s.description | default('', true) | wordwrap(90) }}
{{ evidence_block(s.evidence, claim=s.name + " is a stage of " + d.name) }}
{% endfor %}
{% endif %}
{% else %}*Not curated for this disease.*
{% endif %}

## 11. Management

{% if not (d.treatments or d.clinical_trials or d.surrogate_endpoints) %}*Not curated for this disease.*
{% endif %}
{% if d.treatments %}
| Treatment | Modality | Intent | Status / availability | Agent(s) | Targets / mechanism | Evidence |
|---|---|---|---|---|---|---|
{% for t in d.treatments %}| **{{ cell(t.name) }}**{% if t.description %}<br>{{ cell(t.description) }}{% endif %} | {% if t.therapeutic_modality %}{{ el(t.therapeutic_modality) }}{% else %}—{% endif %} | {{ cell(t.role) }} | — | {{ cell(tx_agents(t)) }} | {{ cell(tx_targets(t)) }} | {{ ev_cell(t.evidence) }} |
{% endfor %}

*Schema gap flagged for review: **Intent** (disease-modifying vs. symptomatic) and
**Status / availability** (approved vs. investigational, with regulatory agency and
drug names by jurisdiction) are not yet first-class fields in dismech, so those columns
are mostly empty. Where known, this information currently sits in the treatment
description. See the cover note for the proposed schema additions.*
{% endif %}
{% if d.clinical_trials %}
### Clinical trials
{% for ct in d.clinical_trials %}
#### {{ ct.name }}
{% if ct.phase %}**Phase:** {{ ct.phase }}{% endif %}{% if ct.status %} | **Status:** {{ ct.status }}{% endif %}

{{ ct.description | default('', true) | wordwrap(90) }}
{{ evidence_block(ct.evidence, claim=ct.name + " is a clinical trial for " + d.name) }}
{% endfor %}
{% endif %}
{% if d.surrogate_endpoints %}
### Surrogate endpoints
{% for se in d.surrogate_endpoints %}
- **{{ se.surrogate_endpoint or se.row_id }}**{% if se.disease_or_use %} — {{ se.disease_or_use }}{% endif %}{% if se.approval_type %} [{{ se.approval_type }}]{% endif %}{% if se.endpoint_validation_level %} | validation: {{ se.endpoint_validation_level }}{% endif %}{% if se.clinical_benefit %}. {{ se.clinical_benefit }}{% endif %}

{% endfor %}
{% endif %}

## 12. Complications

*Not yet modeled in the dismech schema for this disease (complications are partly captured
as downstream causal edges in §6 and as separate comorbidity/trajectory entries).*

## 13. Prevention

*Not yet modeled in the dismech schema.*

## 14. Special populations

*Not yet modeled in the dismech schema (genetic counseling, pediatric, pregnancy, and
other special-population notes are not yet first-class fields).*

## 15. Open questions

{% if d.discussions %}
*This section captures unresolved questions and areas of active investigation — not
deficiencies in anyone's expertise. Many are open across the whole field (e.g. the cause
of sporadic disease, the sources of clinical heterogeneity and their impact on trial
stratification). The framing and grouping of these into themes is still being refined;
input on the categories that matter most to you is very welcome.*

{% for disc in d.discussions %}
### {{ loop.index }}. {{ disc.prompt }}
{% if disc.kind %}**Type:** {{ el(disc.kind) }}{% endif %}{% if disc.status %} | **Status:** {{ el(disc.status) }}{% endif %}

{% if disc.rationale %}{{ disc.rationale | wordwrap(90) }}
{% endif %}{% if disc.attaches_to %}
*Relates to:* {% for a in disc.attaches_to %}`{{ a }}`{% if not loop.last %}, {% endif %}{% endfor %}

{% endif %}{% if disc.proposed_experiments %}
**Proposed experiments to resolve:**
{% for ex in disc.proposed_experiments %}
- {% if ex.name %}**{{ ex.name }}** — {% endif %}{{ ex.description | default(ex.prompt) | default('') }}
{% endfor %}
{% endif %}{% if disc.resolution_note %}**Resolution:** {{ disc.resolution_note }}
{% endif %}{{ evidence_block(disc.evidence, claim="bearing on: " + disc.prompt) }}
{% endfor %}
{% else %}*Not curated for this disease.*
{% endif %}

## 16. Data and model resources

{% if not (d.datasets or d.computational_models or d.animal_models or d.experimental_models) %}*Not curated for this disease.*
{% endif %}
{% if d.datasets %}
### Datasets
{% for ds in d.datasets %}
{% if ds.accession or ds.title %}
#### {{ ds.title | default(ds.accession) }}
{% if ds.accession %}**Accession:** `{{ ds.accession }}`{% endif %}{% if ds.data_type %} | **Type:** {{ ds.data_type }}{% endif %}

{{ ds.description | default('', true) | wordwrap(90) }}
{% if ds.publication %}**Publication:** {{ ds.publication }}{% endif %}

{% endif %}
{% endfor %}
{% endif %}
{% if d.computational_models %}
### Computational models
{% for cm in d.computational_models %}
#### {{ cm.name }}
{% if cm.model_type %}**Type:** {{ cm.model_type }}{% endif %}

{{ cm.description | default('', true) | wordwrap(90) }}
{{ evidence_block(cm.evidence, claim=cm.name + " is a computational model of " + d.name) }}
{% endfor %}
{% endif %}
{% if d.animal_models %}
### Animal models
{% for am in d.animal_models %}
#### {{ am.species }}{% if am.genotype %} -- {{ am.genotype }}{% endif %}

{% if am.category %}**Category:** {{ am.category }}{% endif %}

{{ am.description | default('', true) | wordwrap(90) }}
{{ evidence_block(am.evidence, claim=am.species + " is an animal model for " + d.name) }}
{% endfor %}
{% endif %}
{% if d.experimental_models %}
### Experimental models
{% for em in d.experimental_models %}
#### {{ em.name }}{% if em.experimental_model_type %} ({{ em.experimental_model_type }}){% endif %}

{{ em.description | default('', true) | wordwrap(90) }}
{% if em.findings %}*Findings:* {{ em.findings }}{% endif %}
{{ evidence_block(em.evidence, claim=em.name + " is an experimental model for " + d.name) }}
{% endfor %}
{% endif %}

## 17. Provenance and references

{% if d.notes %}
**Curation notes:** {{ d.notes | wordwrap(90) }}

{% endif %}{% if d.references %}
**Bibliography:**
{% for r in d.references %}
- {{ r.reference }}{% if r.title %} — {{ r.title }}{% endif %}
{% endfor %}

{% endif %}{% if d.curation_history %}
**Change log:**
{% for ev in d.curation_history %}
- {% if ev.curation_timestamp %}{{ ev.curation_timestamp }} — {% endif %}{% if ev.curation_action %}{{ ev.curation_action }}{% endif %}{% if ev.curation_model %} ({{ ev.curation_model }}){% endif %}{% if ev.curation_description %}: {{ ev.curation_description }}{% endif %}
{% endfor %}

{% endif %}*Generated {{ now }} from the dismech knowledge base for expert review. Commit `{{ commit_hash }}`.*

{{ glossary() }}
"""


SCHEMA_PATH = Path(__file__).parent.parent / "src" / "dismech" / "schema" / "dismech.yaml"


def _load_enum_metadata(schema_path, enum_name):
    """Load title and description from a LinkML enum's permissible_values."""
    with open(schema_path) as f:
        schema = yaml.safe_load(f)
    pv = schema.get("enums", {}).get(enum_name, {}).get("permissible_values", {})
    return {
        k: {"title": v.get("title", k), "description": v.get("description", "")}
        for k, v in pv.items()
    }


ENUM_NAMES = [
    "EvidenceSourceEnum",
    "EvidenceItemSupportEnum",
    "FrequencyEnum",
    "ModifierEnum",
    "PenetranceEnum",
    "ExpressivityEnum",
    "ClinicalSignificanceEnum",
    "RegulatoryVariantCategoryEnum",
    "RegulatoryElementTypeEnum",
    "LateralityEnum",
    "MechanisticHypothesisStatusEnum",
    "DiscussionKindEnum",
    "DiscussionStatusEnum",
    "CausalLinkTypeEnum",
    "TherapeuticModalityEnum",
    "TemporalityEnum",
    "ClinicalCourseEnum",
    "OnsetEnum",
    "AbnormalFlagEnum",
    "SeverityEnum",
]

ALL_ENUM_META = {name: _load_enum_metadata(SCHEMA_PATH, name) for name in ENUM_NAMES}

# Convenience aliases
SOURCE_META = ALL_ENUM_META["EvidenceSourceEnum"]
SUPPORT_META = ALL_ENUM_META["EvidenceItemSupportEnum"]
FREQUENCY_META = ALL_ENUM_META["FrequencyEnum"]

# Build a flat lookup: enum_value -> (enum_name, title, description)
_FLAT_ENUM_LOOKUP = {}
for enum_name, meta in ALL_ENUM_META.items():
    for value, info in meta.items():
        if value not in _FLAT_ENUM_LOOKUP:
            _FLAT_ENUM_LOOKUP[value] = (enum_name, info["title"], info["description"])


class GlossaryCollector:
    """Tracks which enum values are used and assigns footnote numbers."""

    def __init__(self):
        self._used = {}  # (enum_name, value) -> footnote number
        self._counter = 0

    def ref(self, enum_name, value):
        """Return the footnote number for a used enum value, registering it if new."""
        key = (enum_name, value)
        if key not in self._used:
            self._counter += 1
            self._used[key] = self._counter
        return self._used[key]

    def render_glossary(self):
        """Render the glossary as an endnote-style reference list."""
        if not self._used:
            return ""
        lines = ["\n### Glossary\n"]
        for (enum_name, value), num in sorted(self._used.items(), key=lambda x: x[1]):
            meta = ALL_ENUM_META.get(enum_name, {}).get(value, {})
            title = meta.get("title", value)
            desc = meta.get("description", "")
            lines.append(f"^{num}^ **{title}**: {desc}\n")
        return "\n".join(lines)


# Module-level collector instance, reset per render
_glossary = GlossaryCollector()


def freq(value):
    """Convert a frequency enum value to a human-readable label with footnote."""
    if not value:
        return ""
    return enum_label(value, "FrequencyEnum")


def freq_lower(value):
    """Like freq() but lowercased for mid-sentence use."""
    if not value:
        return ""
    result = enum_label(value, "FrequencyEnum")
    if result and result[0].isupper():
        return result[0].lower() + result[1:]
    return result


def article(text):
    """Return 'a' or 'an' + text based on the first letter."""
    if not text:
        return "a"
    first = text.lstrip().lstrip("*_")[0:1].lower()
    return f"an {text}" if first in "aeiou" else f"a {text}"


def enum_label(value, enum_name_hint=None):
    """Convert any enum value to a human-readable label with glossary footnote."""
    if not value:
        return ""
    if enum_name_hint and enum_name_hint in ALL_ENUM_META:
        meta = ALL_ENUM_META[enum_name_hint].get(value, {})
        if meta:
            title = meta["title"]
            ref = _glossary.ref(enum_name_hint, value)
            return f"{title}^{ref}^"
    # Fall back to flat lookup
    if value in _FLAT_ENUM_LOOKUP:
        enum_name, title, _ = _FLAT_ENUM_LOOKUP[value]
        ref = _glossary.ref(enum_name, value)
        return f"{title}^{ref}^"
    return value


def evidence_block(evidence, claim="", indent=0):
    """Render a list of evidence items as markdown."""
    if not evidence:
        return ""
    prefix = "  " * indent
    if claim:
        header = f"**Evidence** (*{claim.strip()}*)"
    else:
        header = "**Evidence**"
    lines = [f"\n{prefix}{header}:\n"]
    for i, e in enumerate(evidence, 1):
        ref = e.get("reference", "?")
        supports = e.get("supports", "?")
        source = e.get("evidence_source", "?")
        snippet = e.get("snippet", "")
        explanation = e.get("explanation", "")

        support_title = SUPPORT_META.get(supports, {}).get("title", supports)
        source_title = SOURCE_META.get(source, {}).get("title", source)
        support_ref = _glossary.ref("EvidenceItemSupportEnum", supports) if supports in SUPPORT_META else None
        source_ref = _glossary.ref("EvidenceSourceEnum", source) if source in SOURCE_META else None

        support_str = f"{support_title}^{support_ref}^" if support_ref else support_title
        source_str = f"{source_title}^{source_ref}^" if source_ref else source_title

        lines.append(f"{prefix}{i}. **{ref}** -- {support_str} [{source_str}]\n")
        if snippet:
            lines.append(f'{prefix}   Quote:\n\n{prefix}   > "{snippet.strip()}"\n')
        if explanation:
            lines.append(f"{prefix}   Interpretation: *{explanation.strip()}*\n")
    return "\n".join(lines)


def _safe_wordwrap(text, width=79):
    """None-tolerant word wrap that preserves existing paragraph breaks."""
    if not text:
        return ""
    out = []
    for line in str(text).splitlines():
        out.append(textwrap.fill(line, width=width) if line.strip() else line)
    return "\n".join(out)


_SUPERSCRIPT_DIGITS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def _superscripts_to_unicode(text):
    """Convert pandoc-style ^N^ footnote markers to Unicode superscript glyphs.

    Google Docs' markdown paste does not understand pandoc superscript syntax, so the
    raw ``^1^`` would appear literally. Real superscript characters paste cleanly.
    """
    return re.sub(
        r"\^(\d+)\^",
        lambda m: m.group(1).translate(_SUPERSCRIPT_DIGITS),
        text,
    )


def _cell(text):
    """Sanitize a value for placement inside a single markdown table cell."""
    if text is None:
        return "—"
    s = str(text).replace("\r", " ").replace("\n", " ").replace("|", "\\|").strip()
    return s or "—"


def _enum_title(value):
    """Human-readable title for an enum value, without a glossary footnote."""
    if not value:
        return ""
    if value in _FLAT_ENUM_LOOKUP:
        return _FLAT_ENUM_LOOKUP[value][1]
    return str(value)


def pheno_hpo(ph):
    """HPO id + label (+ modifier) for the phenotype table's term column."""
    t = ph.get("phenotype_term") or {}
    term = t.get("term") or {}
    if not term:
        return "—"
    s = f"`{term.get('id', '')}` {term.get('label', '')}".strip()
    mod = t.get("modifier")
    if mod:
        s += f" [{_enum_title(mod)}]"
    return s


def pheno_quals(ph):
    """Combined qualifier string (severity/temporality/course/onset) for the table."""
    parts = []
    if ph.get("severity"):
        parts.append(f"Severity: {_enum_title(ph['severity']) or ph['severity']}")
    if ph.get("temporality"):
        parts.append(f"Temporality: {_enum_title(ph['temporality'])}")
    if ph.get("clinical_course"):
        parts.append(f"Course: {_enum_title(ph['clinical_course'])}")
    onset = ph.get("onset") or {}
    if onset.get("onset_category"):
        parts.append(f"Onset: {_enum_title(onset['onset_category'])}")
    flags = []
    if ph.get("diagnostic"):
        flags.append("diagnostic")
    if ph.get("excluded"):
        flags.append("excluded")
    if flags:
        parts.append("; ".join(flags))
    return "; ".join(parts)


def ev_cell(evidence):
    """Render a phenotype's evidence list compactly inside one table cell.

    Items are separated by <br><br> (honored in the PDF/HTML path and by Google
    Docs markdown paste); each shows reference, support, source, quote, interpretation.
    """
    if not evidence:
        return "—"
    parts = []
    for e in evidence:
        ref = e.get("reference", "?")
        supports = e.get("supports")
        source = e.get("evidence_source")
        sup = SUPPORT_META.get(supports, {}).get("title", supports) if supports else None
        src = SOURCE_META.get(source, {}).get("title", source) if source else None
        meta = ", ".join(x for x in (sup, src) if x)
        seg = f"**{ref}**" + (f" ({meta})" if meta else "")
        snippet = (e.get("snippet") or "").strip()
        explanation = (e.get("explanation") or "").strip()
        if snippet:
            seg += f': "{snippet}"'
        if explanation:
            seg += f" — *{explanation}*"
        parts.append(_cell(seg))
    return "<br><br>".join(parts)


def cls_val(value):
    """Extract the classification_value(s) from a classification assignment.

    Each axis (Harrison's chapter, mechanistic category, etc.) is a
    ``ClassificationAssignment`` object — or, for the multivalued axes, a list of
    them — carrying ``classification_value`` plus evidence. Render just the value(s);
    without this the template would dump the raw object/dict.
    """
    if not value:
        return ""
    if isinstance(value, list):
        return ", ".join(v for v in (cls_val(v) for v in value) if v)
    if isinstance(value, dict):
        return str(value.get("classification_value") or "")
    return str(value)


def tx_agents(t):
    """Agent list for a treatment row (from therapeutic_agent on the treatment term)."""
    tt = t.get("treatment_term") or {}
    agents = tt.get("therapeutic_agent") or []
    out = []
    for ag in agents:
        term = ag.get("term") or {}
        label = ag.get("preferred_term") or term.get("label") or ""
        out.append(f"{label} (`{term['id']}`)" if term.get("id") else label)
    return ", ".join(x for x in out if x) or "—"


def tx_targets(t):
    """Target-mechanism summary (+ ASO target) for a treatment row."""
    parts = []
    for tm in t.get("target_mechanisms") or []:
        seg = tm.get("target", "")
        if tm.get("treatment_effect"):
            seg += f" ({tm['treatment_effect']})"
        if seg:
            parts.append(seg)
    aso = t.get("aso_details") or {}
    if aso.get("target_gene"):
        tg = aso["target_gene"].get("preferred_term") or ""
        if tg:
            parts.append(f"ASO target: {tg}")
    return "; ".join(parts) or "—"


class DotDict(dict):
    """Dict that returns None for missing keys and supports dot access."""

    def __getattr__(self, key):
        val = self.get(key)
        if isinstance(val, dict):
            return DotDict(val)
        if isinstance(val, list):
            return [DotDict(v) if isinstance(v, dict) else v for v in val]
        return val

    def __getitem__(self, key):
        val = super().get(key)
        if isinstance(val, dict):
            return DotDict(val)
        if isinstance(val, list):
            return [DotDict(v) if isinstance(v, dict) else v for v in val]
        return val

    def get(self, key, default=None):
        val = super().get(key, default)
        if isinstance(val, dict):
            return DotDict(val)
        if isinstance(val, list):
            return [DotDict(v) if isinstance(v, dict) else v for v in val]
        return val


def main():
    parser = argparse.ArgumentParser(description="Render disorder YAML to PDF for expert review")
    parser.add_argument("yaml_file", help="Path to disorder YAML file")
    parser.add_argument("-o", "--output", help="Output PDF path (default: same name as YAML)")
    parser.add_argument("--md-only", action="store_true", help="Output markdown only, no PDF")
    parser.add_argument(
        "--gdocs",
        action="store_true",
        help="Google-Docs-friendly markdown: convert ^N^ footnotes to Unicode "
        "superscripts so they paste cleanly (implies --md-only)",
    )
    args = parser.parse_args()
    if args.gdocs:
        args.md_only = True

    yaml_path = Path(args.yaml_file)
    with open(yaml_path) as f:
        data = DotDict(yaml.safe_load(f))

    # Reset the glossary collector for each render
    global _glossary
    _glossary = GlossaryCollector()

    env = Environment(autoescape=False)
    # None-safe wordwrap: Jinja's built-in is an environment-filter that raises on None
    # descriptions, which are common in optional free-text slots across the KB.
    env.filters["wordwrap"] = _safe_wordwrap
    env.filters["aslist"] = lambda v: v if isinstance(v, list) else ([] if v is None else [v])
    env.globals["evidence_block"] = evidence_block
    env.globals["freq"] = freq
    env.globals["freq_lower"] = freq_lower
    env.globals["article"] = article
    env.globals["el"] = enum_label
    env.globals["cell"] = _cell
    env.globals["pheno_hpo"] = pheno_hpo
    env.globals["pheno_quals"] = pheno_quals
    env.globals["ev_cell"] = ev_cell
    env.globals["tx_agents"] = tx_agents
    env.globals["tx_targets"] = tx_targets
    env.globals["cls_val"] = cls_val
    env.globals["glossary"] = lambda: _glossary.render_glossary()
    template = env.from_string(TEMPLATE)

    # Get current git commit hash
    try:
        commit_hash = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, cwd=yaml_path.parent
        ).stdout.strip() or "unknown"
    except Exception:
        commit_hash = "unknown"

    md = template.render(
        d=data,
        now=datetime.now().strftime("%Y-%m-%d %H:%M"),
        commit_hash=commit_hash,
    )
    # Clean up excessive blank lines
    while "\n\n\n" in md:
        md = md.replace("\n\n\n", "\n\n")

    if args.gdocs:
        md = _superscripts_to_unicode(md)

    if args.md_only:
        out = Path(args.output) if args.output else yaml_path.with_suffix(".md")
        out.write_text(md)
        print(f"Markdown written to {out}")
        return

    # Convert markdown to PDF via pandoc
    pdf_path = Path(args.output) if args.output else yaml_path.with_suffix(".pdf")

    with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w") as tmp:
        result = subprocess.run(
            ["pandoc", "-f", "markdown", "-t", "html5", "--standalone",
             "--metadata", f"title={data.name}",
             "--css", "/dev/null"],
            input=md, capture_output=True, text=True
        )
        if result.returncode != 0:
            print(f"Pandoc error: {result.stderr}")
            return

        html = result.stdout.replace("</head>", REVIEW_CSS + "</head>")
        tmp.write(html)
        tmp_path = tmp.name

    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    subprocess.run(
        [chrome, "--headless", "--disable-gpu",
         f"--print-to-pdf={pdf_path}",
         "--print-to-pdf-no-header",
         f"file://{tmp_path}"],
        capture_output=True
    )
    Path(tmp_path).unlink()
    print(f"PDF written to {pdf_path}")


REVIEW_CSS = """
<style>
  @page { margin: 2cm; }
  body {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.5;
    color: #1a1a1a;
    max-width: 48em;
    margin: 0 auto;
    padding: 2em;
  }
  h1 {
    font-size: 22pt;
    border-bottom: 3px solid #0f766e;
    padding-bottom: 0.3em;
    margin-bottom: 0.5em;
    color: #0f766e;
  }
  h2 {
    font-size: 16pt;
    color: #0f766e;
    border-bottom: 1px solid #ccc;
    margin-top: 1.5em;
    padding-bottom: 0.2em;
    page-break-after: avoid;
  }
  h3 {
    font-size: 13pt;
    color: #333;
    margin-top: 1em;
    page-break-after: avoid;
  }
  h4 {
    font-size: 11pt;
    color: #555;
    margin-top: 0.8em;
  }
  p { margin: 0.4em 0; }
  blockquote {
    border-left: 3px solid #0f766e;
    margin: 0.5em 0;
    padding: 0.3em 0.8em;
    background: #f0fdfa;
    font-style: italic;
    font-size: 10pt;
    color: #333;
  }
  code {
    font-family: 'SF Mono', 'Menlo', monospace;
    font-size: 9pt;
    background: #f3f4f6;
    padding: 0.1em 0.3em;
    border-radius: 3px;
  }
  strong { color: #111; }
  em { color: #444; }
  ul, ol { margin: 0.3em 0; padding-left: 1.5em; }
  li { margin: 0.2em 0; }
  hr {
    border: none;
    border-top: 2px solid #e5e7eb;
    margin: 1.5em 0;
  }
  li + li { page-break-before: avoid; }
  table {
    border-collapse: collapse;
    width: 100%;
    /* Auto layout (not table-layout: fixed) so the content-heavy Evidence column
       in the wide phenotype/treatment tables gets proportionally more width than
       short columns like Modality; word-break below stops long tokens overflowing. */
    font-size: 8.5pt;
    margin: 0.8em 0;
  }
  th, td {
    border: 1px solid #d1d5db;
    padding: 0.3em 0.4em;
    vertical-align: top;
    text-align: left;
    overflow-wrap: break-word;
    word-break: break-word;
  }
  th { background: #f0fdfa; color: #0f766e; }
  /* Evidence inside table cells is rendered inline by ev_cell(), not as Markdown
     blockquotes. This hides any stray blockquote that a future template change
     might route through a cell (e.g. evidence_block output) so it can't break the
     table layout — if you ever *want* blockquotes in cells, remove this rule. */
  td blockquote { display: none; }
</style>
"""


if __name__ == "__main__":
    main()
