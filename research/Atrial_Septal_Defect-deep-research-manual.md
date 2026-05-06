# Atrial Septal Defect Deep Research Fallback

**Provider:** manual fallback

**Rationale:** The requested Falcon workflow was attempted twice from the
worktree after creating the initial YAML. Both runs started but remained silent
without creating a report. The required `cyberian` fallback was then attempted
and exited with code 137 before producing a report. A final `openai` provider
attempt failed immediately because that provider is not available in this
environment. This manual fallback therefore records the PubMed-backed sources
used for curation.

## Key Findings

- ASD is a congenital cardiovascular disorder involving true oval-fossa atrial
  septal deficiency or related interatrial communications, all unified by
  atrial-level mixing of systemic and pulmonary venous blood.
- The dominant physiology is left-to-right shunting with right-sided volume
  overload. Children typically have left-to-right shunting and dilated right
  heart structures, while adults diagnosed late may have pulmonary artery
  hypertension and ventricular dysfunction.
- Untreated significant secundum ASD can lead to exercise intolerance,
  supraventricular arrhythmias, right ventricular dysfunction, pulmonary
  arterial hypertension, and reduced life expectancy.
- Right-sided volume overload can drive atrial electrical remodeling,
  predisposing to atrial tachyarrhythmias and conduction disorders.
- Closure is indicated for significant shunts except in severe irreversible
  pulmonary arterial hypertension. Transcatheter closure is generally preferred
  for suitable secundum ASDs; surgical repair remains valid when device closure
  is unsuitable or anatomy is non-secundum.
- Rare familial ASD can involve cardiac transcription-factor genes including
  NKX2-5 and GATA4, but these findings should not be overgeneralized to most
  sporadic isolated ASD.

## Sources Used

- PMID:22368625, a morphologic review distinguishing true atrial septal defects
  from related interatrial communications and supporting ASD subtype modeling.
- PMID:30305948, a hemodynamic review supporting left-to-right shunting, right
  heart dilation, late pulmonary artery hypertension, and echocardiographic
  assessment.
- PMID:30305954, a rhythm review supporting right-sided volume overload,
  electrical remodeling, arrhythmia risk, and transcription-factor associations.
- PMID:25884091, an adult secundum ASD review supporting natural history,
  closure indications, and transcatheter versus surgical closure.
- PMID:15350172, a transcatheter closure review supporting lower morbidity and
  device-based closure.
- PMID:20932824, a family and functional study supporting rare NKX2-5-associated
  ASD with conduction disease and noncompaction.
- PMID:20659440, a family study supporting rare GATA4-associated ASD.

## Curation Notes

- Evidence snippets were taken from abstracts fetched into `references_cache/`
  by `just fetch-reference`.
- Ontology labels were checked with OAK for HP, GO, CL, UBERON, MAXO, and HGNC
  terms. Conservative preferred-term wording was used where procedure terms were
  broader than the clinical intervention.
- No `references_cache/*.md` files were hand-created or hand-edited.
