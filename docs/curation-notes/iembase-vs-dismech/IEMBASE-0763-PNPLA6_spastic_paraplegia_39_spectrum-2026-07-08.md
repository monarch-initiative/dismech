# IEMbase 0763: PNPLA6-related spastic paraplegia type 39

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 763 |
| Nosology | 14.5.01.13 |
| Nosology code | IEM0672 |
| Gene | PNPLA6 |
| External IDs | OMIM:215470; OMIM:275400; OMIM:612020; ORPHA:139480 |
| Generated mapping | UNMAPPED; weak candidate `Boucher-Neuhauser_Syndrome.yaml` |
| Candidate DisMech targets | `Boucher-Neuhauser_Syndrome.yaml` |
| Review date | 2026-07-08 |

## IEMbase phenotype signal

IEMbase labels this autosomal recessive record as PNPLA6-related spastic
paraplegia type 39, with alternate names Oliver-McFarlane syndrome,
Boucher-Neuhauser syndrome, and Laurence-Moon syndrome. The rows capture a
PNPLA6 spectrum presentation with adult-predominant cerebellar atrophy,
chorioretinal degeneration, peripheral neuropathy, spastic paraparesia or
paraplegia or tetraplegia, hypogonadotropic hypogonadism, growth hormone
deficiency, hypothyroidism, cognitive dysfunction, and nonprogressive
cerebellar ataxia.

## DisMech phenotype coverage

`Boucher-Neuhauser_Syndrome.yaml` is not just a weak lexical match. Although
the file is named for Boucher-Neuhauser syndrome, its description explicitly
models the PNPLA6-disorder spectrum, including Gordon Holmes syndrome,
Oliver-McFarlane syndrome, Laurence-Moon syndrome, and spastic paraplegia type
39. It captures PNPLA6/NTE esterase loss, phospholipid homeostasis disruption,
cerebellar ataxia, cerebellar atrophy, hypogonadotropic hypogonadism or
anterior hypopituitarism, chorioretinal dystrophy, visual impairment,
peripheral axonal neuropathy, spasticity, and cognitive impairment.

## Concordance and completeness

Judgement: false negative / partial local coverage through a PNPLA6-spectrum
entry.

The local target is biologically appropriate for IEMbase's broad PNPLA6 record,
but the filename and primary disease label are narrower than IEMbase's
spastic-paraplegia-type-39 framing. IEMbase reinforces that the local BNS entry
is being used as a spectrum-level target and adds explicit GH deficiency,
hypothyroidism, and spastic paraplegia/tetraplegia wording.

## Curation actions

- Treat `Boucher-Neuhauser_Syndrome.yaml` as meaningful PNPLA6-spectrum
  coverage, not as an unrelated weak candidate.
- Consider whether DisMech should rename, alias, or cross-link the entry more
  explicitly as a PNPLA6 disorder spectrum / SPG39 target.
- Preserve the IEMbase endocrine rows for growth hormone deficiency and
  hypothyroidism when refining subtype-level phenotype completeness.
