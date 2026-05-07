---
disorder: Esophageal_Atresia
research_status: fallback_after_provider_silence
last_updated: "2026-05-07T23:23:53Z"
provider_attempts:
  - provider: falcon
    command: "just research-disorder falcon Esophageal_Atresia"
    result: "terminated_after_quiet_wait_signal_15"
  - provider: openai
    command: "just research-disorder openai Esophageal_Atresia"
    result: "terminated_after_quiet_wait_signal_15"
manual_evidence_scope:
  - ORPHA:1199
  - PMID:20425471
  - PMID:22247246
  - PMID:23877544
  - PMID:27190912
  - PMID:27579697
  - PMID:27993359
  - PMID:31000707
  - PMID:31571760
  - PMID:32515280
---

# Esophageal Atresia Evidence-Backed Research Fallback

## Provider Attempts

The Falcon deep-research command produced no usable output during the bounded
wait and was terminated with signal 15. A secondary OpenAI deep-research attempt
also remained silent during the bounded wait and was terminated with signal 15.
No provider artifact was used for curation.

## Evidence Synthesis

ORPHA:1199 defines esophageal atresia as interruption of esophageal continuity
with or without persistent tracheal communication. The structured Orphanet cache
also provides neonatal onset, European and United States prevalence bands,
synonyms, exact MeSH and OMIM cross-references, and phenotype-frequency rows for
tracheoesophageal fistula, dysphagia, excessive salivation, feeding difficulty,
failure to thrive, recurrent respiratory infections, restrictive ventilatory
defect, gastrointestinal dysmotility, gastroesophageal reflux, respiratory
distress, aspiration, esophagitis, and absent fetal stomach bubble.

PMID:22247246 provides independent population-based EUROCAT support for
prevalence, prenatal detection, associated anomalies, live-born frequency, and
early survival in European regions.

PMID:31000707 is the central disease-primer source. It supports incomplete
foregut compartmentalization as the developmental cause, common
tracheoesophageal fistula association, surgical restoration of esophageal
continuity with TEF ligation/division, long-term gastrointestinal and
respiratory morbidity, post-repair esophageal dysmotility, and diagnostic tools
including high-resolution impedance manometry and pH-multichannel intraluminal
impedance testing.

PMID:32515280 and PMID:20425471 provide developmental mechanism context. They
support the shared anterior foregut origin of trachea and esophagus, disrupted
foregut compartmentalization in EA/TEF, and model-organism evidence implicating
multiple signaling pathways and transcription factors, including sonic
hedgehog/smoothened pathway effectors, in foregut embryogenesis.

PMID:27190912 and PMID:31571760 support newborn diagnosis by failed or
misleading nasogastric-tube passage and chest/abdominal radiography with the
tube arrested in the upper esophageal pouch. PMID:31571760 also supports using
the radiograph to estimate esophageal gap length before repair.

PMID:27993359 supports contemporary surgical cohort context: most infants have
proximal EA with distal TEF, surgical repair is esophageal reconstruction with
or without TEF ligation, postoperative morbidity is common, and perioperative
practice varies substantially across centers.

PMID:27579697 provides guideline support for long-term care of reflux,
dysphagia, feeding difficulty, anastomotic strictures, congenital esophageal
stenosis, and other gastrointestinal complications after EA/TEF repair.
PMID:23877544 provides systematic-review support for fluoroscopic or endoscopic
balloon dilatation as primary treatment for anastomotic strictures after
esophageal atresia repair.

## Scope Confirmation

The YAML intentionally emphasizes the core congenital esophageal atresia/TEF
phenotype and direct aerodigestive sequelae. It does not import every Orphanet
occasional or rare associated anomaly because many reflect syndromic or VACTERL
contexts rather than the core disorder mechanism.
