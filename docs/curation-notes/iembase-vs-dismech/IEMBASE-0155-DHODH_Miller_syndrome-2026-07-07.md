# IEMbase 0155: DHODH-related Miller syndrome

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 155 |
| Nosology | 16.1.02.01 |
| Gene | DHODH |
| External IDs | OMIM:263750; OMIM:126064; ORPHA:246 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | `Pyruvate_Dehydrogenase_Deficiency.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as DHODH-related dihydroorotate dehydrogenase
deficiency, with alternate labels postaxial acrofacial dysostosis, Miller
syndrome, Genee-Wiedemann syndrome, and POADS. Treatability is marked unknown.

The biochemical rows report increased urinary dihydro-orotic acid and orotic
acid, with variable orotidine and N-carbamyl aspartate. The clinical signal is
a congenital malformation syndrome: cleft lip/palate, micrognathia, malar
hypoplasia, cup-shaped and low-set ears, conductive deafness, coloboma,
postaxial limb hypoplasia or absence of fifth digits, syndactyly, radioulnar
synostosis, rib defects, supernumerary vertebrae, hip dislocation, renal
anomalies, cryptorchidism, micropenis, midgut malrotation, pyloric stenosis,
pectus excavatum, and accessory nipples.

## DisMech phenotype coverage

There is no valid local Miller syndrome / DHODH disease entry.

`Pyruvate_Dehydrogenase_Deficiency.yaml` is a false candidate. It is centered
on PDH-complex genes, impaired pyruvate oxidation, lactic acidosis, Leigh-like
neurologic disease, and ketogenic or thiamine-directed management. It does not
model DHODH, de novo pyrimidine synthesis, dihydroorotate accumulation, or the
postaxial acrofacial dysostosis phenotype bundle.

Some existing developmental-patterning modules may eventually help represent
the craniofacial and limb malformation logic, but there is no current disease
target for this entity.

## Concordance and completeness

Judgement: true local gap.

The IEMbase entry is clearly anchored on DHODH and a congenital craniofacial,
limb, rib, renal, and genital malformation syndrome. The generated pyruvate
dehydrogenase candidate shares broad metabolic wording but not identity,
mechanism, biomarkers, or phenotype structure.

## Curation actions

- Leave IEMbase 155 unmapped for now.
- Future curation should create a DHODH/Miller syndrome entry rather than fold
  this into PDH deficiency.
- Preserve the IEMbase urinary dihydro-orotic acid/orotic acid biomarkers and
  the serial craniofacial-limb malformation pattern as primary leads.
