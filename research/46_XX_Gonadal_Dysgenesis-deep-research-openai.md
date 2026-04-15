---
provider: openai
model: gpt-5
cached: true
start_time: "2026-04-14T05:00:00Z"
end_time: "2026-04-14T05:40:11Z"
duration_seconds: 2411.0
template_file: manual_curation_note
template_variables:
  disease_name: 46_XX_Gonadal_Dysgenesis
  mondo_id: MONDO:0009299
  category: Mendelian
citation_count: 8
---

## Summary

`MONDO:0009299` provides a dedicated disease-level anchor for `46 XX gonadal
dysgenesis`. The literature consistently treats this as a rare, genetically
heterogeneous ovarian developmental failure state in phenotypically female
individuals with a normal `46,XX` karyotype, with the core phenotype defined by
streak or underdeveloped ovaries, absent spontaneous puberty, primary
amenorrhea, uterine hypoplasia, and hypergonadotropic hypogonadism.

## Disease-Anchor Decision

- Anchor chosen: `46 XX gonadal dysgenesis` (`MONDO:0009299`)
- Why this anchor: the disease has its own MONDO term and multiple primary
  human papers describe it as a coherent clinical entity rather than only as a
  phenotype mention inside broader DSD literature.
- Why not a generic `46,XX DSD` bucket: the core disease definition here is
  ovarian developmental failure with phenotypically female external genitalia,
  not generic 46,XX sex-development variation such as prenatal androgen excess.
- Why not lump fully with broader primary ovarian insufficiency: `NR5A1`
  demonstrates overlap with `46,XX primary ovarian insufficiency`, but the
  `46,XX gonadal dysgenesis` literature is narrower and emphasizes congenital
  streak/underdeveloped ovaries, absent spontaneous puberty, and uterine
  hypoplasia.
- Why not split into single-gene disorders for this issue: `NUP107`,
  `PSMC3IP`, `FSHR`, and `NR5A1` all support the same disease-level anchor, and
  the issue explicitly asked for a disease-level dismech entry rather than a
  single-gene subtype.

## Mechanistic Themes

- Shared proximal theme: disrupted female gonad development.
- Shared intermediate theme: impaired ovarian hormonal signaling and
  folliculogenesis.
- Shared downstream theme: streak or severely underdeveloped ovaries leading to
  hypoestrogenic hypergonadotropic ovarian failure.

## Papers Used for YAML Evidence

| PMID | Use in YAML | Key contribution |
| --- | --- | --- |
| 23087880 | prevalence framing | Rare genetically heterogeneous disease framing |
| 26485283 | case definition, pathophysiology, phenotypes, genetics | Strong disease-definition abstract plus ovarian-development mechanism |
| 21963259 | progression, pathophysiology, phenotypes, genetics | Streak gonads, estrogenic signaling, follicular-pool mechanism |
| 7553856 | pathophysiology, genetics | Direct FSHR signaling defect causing ovarian dysgenesis |
| 8855829 | pathophysiology, phenotypes | Elevated FSH/LH and amenorrhea in mechanistically defined subset |
| 19246354 | pathophysiology, genetics | Overlap boundary with broader ovarian insufficiency |
| 35142292 | treatment | Hormone replacement therapy for secondary sexual characteristics and osteoporosis prevention |
| 31809259 | PR framing / differential context | MRKH misdiagnosis pitfall and estrogen-dependent uterine visualization |

## Curation Notes

- Evidence snippets were restricted to exact quoted text from the cached PMID
  records.
- The YAML intentionally avoids generic DSD-management statements as primary
  treatment evidence; management is limited to hormone replacement therapy with
  direct PMID-backed wording.
- The YAML intentionally avoids assigning phenotype frequency bands because the
  available abstracts support association but not robust quantitative frequency.
