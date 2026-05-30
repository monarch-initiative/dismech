---
provider: scanner
model: claude-opus-4-7
cached: true
start_time: '2026-05-18T00:00:00Z'
end_time: '2026-05-18T00:00:00Z'
duration_seconds: 0
template_file: templates/disease_pathophysiology_research_scanner.md
template_variables:
  disease_name: Hepatic Fibrinogen Storage Disease
  mondo_id: MONDO:0018060
  category: Genetic
provider_config:
  source: cached_references
  references_used:
  - PMID:33105716
  - PMID:31965886
  - PMID:36055263
---

## Question

Pathophysiology and clinical mechanisms of Hepatic Fibrinogen Storage Disease
(HFSD; also hereditary hypofibrinogenemia with hepatic storage, HHHS). Core
disease mechanisms, molecular and cellular pathways, involved genes and
proteins, affected cell types and anatomical structures, disease progression,
major clinical phenotypes and complications, modifier genes, and
treatment-relevant mechanism papers. Distinguish this toxic gain-of-function
ER-storage entity from simple (Type I) loss-of-function hypofibrinogenemia.

## Output

# Scanner Research Synthesis: Hepatic Fibrinogen Storage Disease (HFSD / HHHS)

This report is a literature synthesis built strictly from the cached reference
abstracts available in `references_cache/` (PMID:33105716, PMID:31965886,
PMID:36055263). No external deep-research provider was invoked; every statement
below is grounded in one of these three cached sources, and PMIDs are cited
inline. It is intended as a curation input for
`kb/disorders/Hepatic_Fibrinogen_Storage_Disease.yaml`.

---

## Disease Identity

- **Preferred name**: Hepatic fibrinogen storage disease (HFSD); synonyms
  hereditary hypofibrinogenemia with hepatic storage (HHHS), fibrinogen
  storage disease (FSD) (PMID:33105716).
- **MONDO**: MONDO:0018060 (congenital fibrinogen deficiency) used as the
  resolvable parent; the specific term MONDO:7770747 (hepatic fibrinogen
  storage disease) did not yet resolve in the released OAK sqlite cache at
  curation time.
- **Disease class**: HFSD belongs to the **ER storage diseases (ERSDs)** —
  inborn errors of metabolism involving secretory proteins, characterized by
  hepatocellular storage in the rough ER and plasma deficiency of the relevant
  protein; ERSDs comprise alpha-1-antitrypsin, fibrinogen, and
  alpha-1-antichymotrypsin deficiencies (PMID:33105716).
- **Mechanistic contrast**: Unlike simple Type I quantitative
  hypofibrinogenemia (a loss-of-function defect with a structurally normal
  liver), HFSD is a **toxic gain-of-function** disorder in which the mutant
  fibrinogen is assembled but secretion-incompetent, polymerizes, and
  aggregates spontaneously within the hepatocyte ER (PMID:33105716). The
  congenital fibrinogen disorders are formally classified by clottable and
  antigenic fibrinogen levels together with clinical phenotype and genotype
  (PMID:36055263).

---

## Core Pathophysiology

### Genetic mechanism

HFSD is caused by **heterozygous missense mutations located exclusively in
exons 8 and 9 of FGG** (the fibrinogen γ-chain gene); eight FGG mutations had
been reported at the time of the cached review, seven non-conservative missense
substitutions plus one 14-nucleotide deletion activating a cryptic splice site
(PMID:33105716). All affected residues lie in the highly conserved C-terminal
globular **γ module** (residues ~310–401), and **all mutations occur in the
heterozygous state**, supporting an autosomal dominant trait and indirectly
suggesting homozygous lethality (PMID:33105716). Variants are named after the
proband's city of origin (e.g., Aguadilla, Brescia, Angers, Beograd, Ankara,
Pisa); **Aguadilla is the most common worldwide** (PMID:33105716;
PMID:31965886).

### Molecular cascade

1. **Mutant γ-chain production** — destabilizing FGG γ-module missense variant
   produced in the heterozygous state (PMID:33105716).
2. **Hepatocellular ER aggregation** — mutant fibrinogen retains
   polymerization ability but cannot be secreted, so it aggregates
   spontaneously within the rough ER of hepatocytes as densely packed tubular
   inclusions (PMID:33105716). A proposed structural mechanism invokes a
   serpin-like β-strand "pull-out" from the central β-sheet of the γ module,
   permitting polymerization of destabilized fibrinogen (PMID:33105716).
3. **Histologic inclusions** — circular eosinophilic intracytoplasmic
   inclusion bodies, fibrinogen-immunoreactive, classified ultrastructurally
   into type I (fingerprint tubular), type II (ground-glass), and type III
   (mixed) deposits (PMID:33105716); a concrete case showed "circular
   eosinophil inclusion bodies in the hepato-cytoplasm" (PMID:31965886).
4. **ER stress / impaired proteostasis** — accumulated polymers impose
   proteotoxic ER burden; **autophagy is the main pathway for intracellular
   fibrinogen clearance**, and defects in protein-degradation pathways are
   candidate disease modifiers (PMID:33105716).
5. **Hepatocyte injury** — ER accumulation "strongly predisposes to the
   development of chronic liver disease of variable severity, both in children
   and adults" (PMID:33105716).
6. **Stellate-cell-mediated fibrogenesis** — the injury/regeneration cycle
   drives hepatic fibrosis; patients show "tremendous variability in the
   severity of liver disease, going from no signs of injury, to mild/moderate
   liver fibrosis, up to cirrhosis" (PMID:33105716). The conserved
   TGF-beta/Smad mesenchymal-activation axis is modeled by `conforms_to`
   linkage to the `fibrotic_response` module.
7. **Secondary hypofibrinogenemia** — retention rather than secretion lowers
   circulating fibrinogen; HFSD is defined by "hypofibrinogenemia, as well as
   the retention of variant fibrinogen within the hepatocellular endoplasmic
   reticulum" (PMID:31965886).

### Key liver biology

Fibrinogen is a 340-kDa hexamer (two sets of Aα/Bβ/γ trimers) coded by FGA,
FGB, FGG on chromosome 4q31.3, assembled in the ER (with calnexin/calreticulin
and ERp57 chaperones) and mainly expressed in liver (PMID:33105716). In HFSD
the liver is the principal target organ; the coagulopathy is secondary and
clinically minor (PMID:33105716).

---

## Clinical Phenotype

- **Elevated hepatic transaminases** — usual presenting feature; HFSD "is
  associated with mild and intermittent hypertransaminasemia" (mean ALT
  191 ± 119 U/L, AST 147 ± 97 U/L) (PMID:33105716); a case showed elevated ALT
  122 IU/L and AST 119 IU/L (PMID:31965886).
- **Hypofibrinogenemia** — defining laboratory feature, secondary to impaired
  secretion (PMID:33105716; PMID:31965886).
- **Hepatic fibrosis / cirrhosis** — variable, from no injury through
  mild/moderate fibrosis up to cirrhosis, sometimes in children
  (PMID:33105716).
- **Hepatomegaly** — "Abdominal ultrasonography showed mild hepatomegaly" in
  an asymptomatic 4-year-old (PMID:31965886).
- **Hypo-apo-β (APOB) proteinemia** — "HHHS has been associated with
  hypo-apo-β (APOB) proteinemia in several cases", with fibrinogen and APOB
  co-accumulating in the same ER inclusions; the absence of APOB/MTTP
  mutations indicates a secondary phenomenon (PMID:33105716).
- **Coagulopathy without bleeding** — "HHHS patients usually show prolonged
  coagulation parameters ... but no hemorrhagic manifestations nor abnormal
  wound healing" (PMID:33105716).
- **Onset** — first symptoms (usually transaminase elevation) at a young age
  (mean 13.1 ± 20.2 years); HFSD equally distributed between sexes
  (PMID:33105716).

---

## Disease Modifiers / Variable Expressivity

The same FGG mutation can behave differently across individuals, even within a
family. Proposed modifiers: (i) genetic defects in protein-degradation /
autophagy pathways governing mutant-fibrinogen clearance; (ii) xenobiotic
intake (estrogen therapy, alcohol); (iii) acute/chronic viral infection and the
acute-phase over-production of fibrinogen "crowding" an already burdened ER
(PMID:33105716). This is a documented mechanistic theme not yet modeled as a
discrete pathophysiology node and is a candidate enrichment.

---

## Genetics Summary

| Gene | HGNC | Role | Mutation class |
|------|------|------|----------------|
| FGG | hgnc:3694 | Causative | Heterozygous missense in exons 8/9 (γ module, residues ~310–401); one cryptic-splice deletion (PMID:33105716) |

**Inheritance**: Autosomal dominant; heterozygous only (PMID:33105716).

---

## Treatment-relevant mechanisms

- **Carbamazepine (autophagy enhancer) + ursodeoxycholic acid** — beneficial
  in some cases; CBZ is "known to enhance autophagy, and its efficacy seems to
  be related to the normalization of ALT levels" (PMID:33105716).
- **Supportive care / monitoring** — fibrinogen supplementation is the
  cornerstone of bleeding management in fibrinogen disorders generally
  (PMID:36055263), but is only rarely required in HFSD given the minimal
  bleeding phenotype (PMID:33105716).
- No HFSD-specific liver transplantation evidence is present in the cached
  abstracts (the prior PR review correctly flagged and removed an
  unsupported transplantation claim).

---

## Content-Completeness Cross-Check vs. current YAML

| Dimension | Status |
|-----------|--------|
| Phenotype coverage | Adequate after enrichment — transaminase elevation, hypofibrinogenemia, hepatic fibrosis, cirrhosis, hepatomegaly, hypo-APOB proteinemia, subclinical coagulopathy all modeled. |
| Subtype completeness | Adequate — single mechanistic entity; FGG city-named alleles are variant-level, not subtypes. |
| Pathophysiology | Adequate — mutant γ-chain → ER aggregation → ER stress/autophagy → hepatocyte injury → stellate-cell activation (conforms_to fibrotic_response#Mesenchymal Cell Activation) → excessive hepatic ECM deposition (conforms_to fibrotic_response#Excessive ECM Deposition) → fibrosis/cirrhosis; secondary hypofibrinogenemia → subclinical coagulation abnormality. Modifier-gene/autophagy-capacity theme is noted in `notes` and remains an optional future node. |
| Treatments | Adequate — CBZ+UDCA and supportive care, both with exact cached-abstract snippets. |
| Genetic | Adequate — FGG causative, exons 8/9, heterozygous dominant. |
| Biomarkers/diagnostics | Description-level only (immunohistochemistry/electron microscopy diagnosis); not formalized as structured biomarkers — optional enrichment. |
| References | Three cached PMIDs; all snippets are exact whitespace-normalized substrings. |

---

## Notes for reviewers

- This artifact is a transparent **scanner cached-reference synthesis**, not an
  external provider narrative; it follows the same format as the sibling
  approved PR for Congenital Hypofibrinogenemia (#2727).
- The conserved TGF-beta/Smad mesenchymal-activation evidence is intentionally
  not duplicated as a disease-specific snippet (the cached HFSD abstracts do
  not mention TGF-beta or stellate cells by name); it is inherited through
  `conforms_to: fibrotic_response#Mesenchymal Cell Activation`, mirroring the
  Wilson's Disease hepatic-fibrosis conformance pattern.
- `disease_term` should be re-pointed from MONDO:0018060 to MONDO:7770747 once
  the OAK mondo cache refreshes (tracked in the entry `notes`).
