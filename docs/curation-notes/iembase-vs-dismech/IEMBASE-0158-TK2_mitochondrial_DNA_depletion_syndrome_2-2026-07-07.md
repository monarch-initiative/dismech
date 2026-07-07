# IEMbase 0158: TK2-related mitochondrial DNA depletion syndrome 2

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 158 |
| Nosology | 9.1.06.01 |
| Gene | TK2 |
| External IDs | OMIM:609560; OMIM:188250; ORPHA:254875 |
| Generated mapping | CANDIDATE to `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml` |
| Candidate DisMech targets | `Mitochondrial_Neurogastrointestinal_Encephalomyopathy.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as TK2-related mitochondrial thymidine kinase 2
deficiency, with alternate labels mitochondrial DNA depletion syndrome type 2
and MTDPS2. Treatability is marked unknown, but the JSON contains a
pharmacological deoxynucleoside treatment row.

The biochemical profile includes increased plasma creatine kinase, increased
plasma lactate, decreased muscle cytochrome c oxidase activity, and increased
histochemical mitochondrial proliferation in muscle. Clinical rows include
muscle mitochondrial DNA depletion, hypotonia, myopathy, ophthalmoplegia or
ophthalmoparesis, peripheral neuropathy, neurological symptoms, spinal muscular
atrophy-like presentation, and perinatal death.

## DisMech phenotype coverage

The generated MNGIE candidate is not a valid mapping. The local MNGIE entry is
anchored on TYMP deficiency, thymidine/deoxyuridine accumulation, and
neurogastrointestinal disease, with POLG and RRM2B listed only as distinct
MNGIE-like phenotypes. It does not model TK2 mitochondrial thymidine kinase 2
deficiency or MTDPS2.

Local references to TK2 occur in `Autosomal_Dominant_Cerebellar_Ataxia_Type_III.yaml`
as part of a BEAN1/TK2-region SCA31 repeat locus. That is an intronic
repeat-associated cerebellar ataxia context, not biallelic TK2 enzyme
deficiency with mitochondrial DNA depletion.

## Concordance and completeness

Judgement: false-positive candidate; true local gap.

The MNGIE candidate shares broad mitochondrial nucleotide-pool and
ophthalmoplegia language, but the disease identity is wrong. IEMbase 158 is a
TK2 myopathic mitochondrial DNA depletion syndrome with CK/lactate, COX
deficiency, mitochondrial proliferation, mtDNA depletion, severe hypotonia and
myopathy, and early lethality. That phenotype is not represented by the current
MNGIE or SCA31 entries.

## Curation actions

- Leave IEMbase 158 unmapped for now.
- Future curation should create a TK2/MTDPS2 entry if this disease is in scope.
- Preserve deoxynucleoside therapy, muscle mtDNA depletion, CK/lactate, COX,
  and ophthalmoparesis as key leads for that future entry.
