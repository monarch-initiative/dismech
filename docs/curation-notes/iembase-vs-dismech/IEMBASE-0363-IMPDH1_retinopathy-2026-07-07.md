# IEMbase 0363: IMPDH1-related retinopathy

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 363 |
| Nosology | 16.2.15.01 |
| Gene | IMPDH1 |
| External IDs | OMIM:146690; ORPHA:65 |
| Generated mapping | CANDIDATE/MEDIUM to `GUCY2D-Related_Retinopathy.yaml` |
| Candidate DisMech targets | No exact local target identified |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents IMPDH1-related inosine-5'-monophosphate dehydrogenase
deficiency, with abbreviations PR10 and LCA11 and alternate names retinitis
pigmentosa type 10 and Leber congenital amaurosis type 11. It is listed as an
autosomal dominant disorder.

Characteristic rows include constricted visual fields, a Leber amaurosis-like
presentation, pigmentary retinopathy, retinal bone-corpuscle pigmentation,
retinal dysfunction, retinal dystrophy, retinitis pigmentosa, and vision
loss/optic atrophy. Additional clinical rows include night blindness and
nystagmus. IEMbase lists no biochemical or treatment rows.

## DisMech phenotype coverage

The generated GUCY2D retinopathy candidate should be rejected. GUCY2D-related
retinopathy is a phototransduction/cGMP retinal guanylate cyclase disorder, not
an IMPDH1 inosine monophosphate dehydrogenase disease. The shared inherited
retinal dystrophy phenotype is not enough for a gene-level or disease-level
mapping.

No exact IMPDH1 retinopathy DisMech disease file was identified. Local inherited
retinal degeneration or GUCY2D/RHO context may be phenotype-family context only.

## Concordance and completeness

Judgement: true local gap; reject the generated GUCY2D candidate.

IEMbase supplies a coherent IMPDH1 retinal disease signal: IMPDH1 identity,
autosomal dominant inheritance, retinitis pigmentosa type 10, Leber congenital
amaurosis type 11, constricted visual fields, night blindness, nystagmus,
pigmentary/bone-spicule retinopathy, retinal dysfunction/dystrophy, and vision
loss.

## Curation actions

- Do not map this record to `GUCY2D-Related_Retinopathy.yaml`.
- Create or prioritize a future IMPDH1 retinopathy target if this disease enters
  active DisMech curation.
- If a future entry reuses shared retinal-degeneration module context, keep the
  disease-specific proximal mechanism separate from GUCY2D phototransduction
  biology.
