# Autosomal Dominant Polycystic Kidney Disease Deep Research Fallback

## Provider Attempts

- 2026-05-08T16:24Z: Falcon deep-research was invoked directly with
  `deep-research-client research` for Autosomal dominant polycystic kidney
  disease (`MONDO:0004691`) because `just research-disorder` requires an
  existing YAML file. The command produced no output for approximately two
  minutes and was terminated.
- 2026-05-08T16:27Z: OpenAI deep-research fallback was invoked with the same
  template and variables. The command produced no output for approximately 90
  seconds and was terminated.

No provider-generated deep-research artifact was available. Curation therefore
proceeded from exact, locally cached evidence and the structured ORPHA:730
record. No `references_cache/*.md` files were hand-created or hand-edited.

## Evidence Scope Used For Curation

- ORPHA:730 — structured Orphanet record for Autosomal dominant polycystic
  kidney disease. Used for the exact MONDO mapping, disease definition,
  disease-causing gene rows, and HPO phenotype-frequency rows.
- PMID:40126492 — 2025 JAMA clinical review. Used for current prevalence,
  causal-gene proportions, major clinical frequencies (hepatic cysts,
  hypertension, intracranial aneurysm), progression to kidney replacement
  therapy, Mayo Imaging Classification, blood-pressure/sodium management, and
  tolvaptan effect size.
- PMID:26718155 — clinical/pathogenesis review. Used for the PKD1/PKD2
  loss-of-function framing and progressive renal-cyst phenotype.
- PMID:26877954 — full-text mechanistic review on cyst growth, polycystins,
  and primary cilia. Used for the main pathophysiology chain: polycystin
  dosage loss at renal epithelial primary cilia, cilium-dependent
  cyst-promoting signal disinhibition, reduced calcium/increased cAMP
  signaling, epithelial proliferation, chloride-driven secretion, cyst
  expansion, fibrosis, parenchymal destruction, and renal failure.
- PMID:23121377 / clinicaltrials:NCT00428948 — TEMPO 3:4 phase 3 tolvaptan
  trial. Used for the tolvaptan treatment entry, mechanism target, outcome
  evidence, and clinical-trial section.
- PMID:16932388, PMID:10926175, and PMID:35253003 were reviewed as background
  scope for primary cilia, calcium homeostasis, Wnt/cAMP/Ras/MAPK signaling,
  two-hit pathogenesis, and JNK signaling, but were not cited directly in the
  YAML because the main cilium/cAMP pathway and clinical management claims were
  better supported by PMID:26877954, PMID:40126492, and PMID:23121377.

## Curation Conclusions

ADPKD is best modeled as a renal epithelial ciliopathy in which reduced dosage
or loss of PKD1/PKD2 polycystins and rarer polycystin-biogenesis/ciliary genes
disrupt the polycystin receptor-channel complex at the primary cilium. The
proximal consequence is loss of tonic suppression of a cilium-dependent
cyst-promoting signal, accompanied by reduced cellular calcium signaling and
increased intracellular cAMP. Elevated cAMP activates protein kinase A and
supports epithelial proliferation plus chloride-driven fluid secretion,
expanding epithelial-lined renal cysts. Progressive cyst expansion produces
massive kidney enlargement, fibrosis/extracellular-matrix accumulation,
destruction of renal parenchyma, declining GFR, elevated creatinine, chronic
kidney disease, and kidney failure.

The curation prioritizes the major Orphanet clinical features: very frequent
renal cysts, renal insufficiency, decreased GFR, elevated creatinine, and
hepatic cysts; frequent hypertension, hematuria, chronic kidney disease, stage
5 chronic kidney disease, flank pain, albuminuria, and urinary electrolyte
abnormalities; and clinically important occasional extrarenal/vascular
features including nephrolithiasis, pyelonephritis, pancreatic cysts, mitral
valve prolapse, aortic root aneurysm, cerebral artery dilatation/intracranial
aneurysm, arachnoid cyst, and reproductive findings.

Treatment is represented by disease-modifying tolvaptan pharmacotherapy
targeting the vasopressin/cAMP cyst-growth pathway, plus sodium restriction and
blood-pressure targets as conservative management. Diagnosis is represented by
MRI total-kidney-volume risk stratification through the Mayo Imaging
Classification.
