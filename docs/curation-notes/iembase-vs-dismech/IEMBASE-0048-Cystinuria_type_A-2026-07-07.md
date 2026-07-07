# IEMbase 0048: SLC3A1-related cystinuria type A

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 48 |
| Nosology | 1.11.04.01 |
| Gene | SLC3A1 |
| External IDs | OMIM:220100 |
| Generated mapping | MAPPED by `identifier:OMIM:220100` |
| Candidate DisMech targets | `Cystinuria.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as autosomal recessive SLC3A1-related cystinuria type A.
The listed prevalence is 1:7,000 and treatability is marked yes, although no
specific treatment rows are present in the cached record.

The biochemical pattern is the expected COLA transporter profile: markedly
increased urinary arginine, cystine, lysine, and ornithine from infancy onward,
with low-to-normal plasma arginine, cystine, lysine, and ornithine. The
characteristic clinical feature is cystine urolithiasis, strongest in adulthood.
Additional clinical features include hematuria, obstructive uropathy, chronic
renal failure, and urinary infections.

## DisMech phenotype coverage

The generated mapping to `Cystinuria.yaml` is correct. The local entry models
cystinuria as an SLC3A1 or SLC7A9 proximal tubular cystine/dibasic amino acid
transport disorder and explicitly includes cystinuria type A as the SLC3A1/rBAT
subtype.

DisMech covers the SLC3A1 and SLC7A9 genetic causes, impaired b(0,+) cystine
and dibasic amino acid transport, increased urinary cystine, arginine, lysine,
and ornithine, cystine supersaturation, crystalluria, recurrent cystine
nephrolithiasis, hematuria, recurrent urinary tract infections, renal
insufficiency, hypertension, flank pain, nausea/vomiting, abnormal urinary odor,
hypocitraturia, hypercalciuria, hyperuricosuria, stone composition and urinary
cystine evaluation, and SLC3A1/SLC7A9 genetic testing.

DisMech is also much richer therapeutically: high fluid intake and dietary
sodium/protein moderation, urinary alkalinization with potassium citrate,
cystine-binding thiol drugs such as tiopronin or D-penicillamine, calculi
removal for symptomatic or large stones, and investigational alpha-lipoic acid.

## Concordance and completeness

Judgement: correct mapping and high concordance. If a subtype-level target is
available in downstream tooling, the best target is `Cystinuria.yaml#Cystinuria
type A`; otherwise the file-level mapping is acceptable because type A is
already represented inside the file.

IEMbase adds useful subtype-specific framing and plasma low-to-normal COLA amino
acid values. DisMech adds the broader type A/type B structure, stone chemistry
modifiers, diagnostic detail, chronic complication modeling, and treatment
coverage.

## Curation actions

- Keep the generated mapping to `Cystinuria.yaml`.
- Prefer subtype placement at `Cystinuria.yaml#Cystinuria type A` if the
  crosswalk later supports entity-level subtype anchors.
- Consider adding IEMbase's plasma low-to-normal arginine/cystine/lysine/
  ornithine detail if supported by citable evidence.
- Do not import an empty IEMbase treatment block over the richer DisMech
  management content.
