# Delivery systems: recording what carries a drug

A treatment's **carrier** — the lipid nanoparticle, the liposome, the albumin
particle, the viral vector — is recorded in a `delivery_system` block on the
`Treatment`, alongside any targeting ligand on that carrier and what the carrier
is aimed at.

```yaml
treatments:
- name: Vutrisiran
  therapeutic_modality: SIRNA
  delivery_system:
    delivery_platform: CONJUGATE
    targeting_ligand: GALNAC
    targeting_receptor:
      preferred_term: ASGR1
      term:
        id: hgnc:742
        label: ASGR1
    target_cell_types:
    - preferred_term: hepatocyte
      term:
        id: CL:0000182
        label: hepatocyte
```

## Why this is not inside `oligonucleotide_details`

It used to be. `delivery_platform` and `conjugation` were slots of
`OligonucleotideDetail`, reachable only from a `Treatment` whose
`therapeutic_modality` was `ANTISENSE_OLIGONUCLEOTIDE` or `SIRNA`. That put the
carrier axis inside the payload chemistry, and the consequences were visible in
the KB:

- **`nab-sirolimus`** (`Perivascular_Epithelioid_Cell_Neoplasm`) is an FDA-approved
  albumin-bound nanoparticle. Its modality is `SMALL_MOLECULE`, so the carrier
  survived only in a free-text `preferred_term`, `sirolimus albumin-bound
  nanoparticles`.
- **Liposomal irinotecan** in NALIRIFOX (`Pancreatic_Ductal_Adenocarcinoma`) is
  the one component of that regimen that distinguishes it from FOLFIRINOX, and
  that difference is entirely the carrier. Same problem.
- **`MRNA_THERAPY`** has been a permissible `therapeutic_modality` with **zero**
  uses across the KB. It is a modality *defined* by its carrier, and there was
  no slot to name one.

None of those is an oligonucleotide, and a query for "every treatment in the KB
delivered in a nanoparticle" could not have returned any of them.

## The four attributes, and what each claims

| Slot | Claim |
|---|---|
| `delivery_platform` | What carries the agent at all — unformulated, a ligand conjugate, an LNP, a liposome, an albumin particle, a viral vector |
| `targeting_ligand` | What is on the carrier (or on the agent) that drives uptake |
| `targeting_receptor` | The receptor or antigen that ligand binds, bindable to HGNC |
| `target_cell_types` | The cell type the carrier is aimed at, bindable to CL |

**`delivery_platform` and `targeting_ligand` are orthogonal, in both
directions.** Patisiran is `UNCONJUGATED` *and* `LIPID_NANOPARTICLE`; vutrisiran
is `GALNAC` *and* `CONJUGATE`. A nanoparticle may also carry a ligand on its own
surface — an antibody-coated mRNA-LNP is `ANTIBODY` *and* `LIPID_NANOPARTICLE` —
which is the case that motivated generalizing the ligand slot beyond covalent
attachment to an oligonucleotide.

**`LIPOSOME` is not a spelling of `LIPID_NANOPARTICLE`.** The ionizable lipid in
an LNP is what destabilizes the endosomal membrane on acidification and releases
a nucleic-acid payload; a PEGylated phospholipid bilayer vesicle carrying an
already cell-permeant cytotoxic does no such thing. It changes biodistribution
and toxicity instead. Collapsing them would erase the reason one exists.

**An untargeted carrier is a normal record.** A PEGylated liposome accumulates
passively: it has no ligand, no receptor, and no target cell type. Leave those
three slots absent rather than asserting a target the formulation does not have.
Naming a `targeting_receptor` while setting `targeting_ligand: UNCONJUGATED` is
a contradiction and is gated.

**`targeting_receptor` is the receptor, not the ligand.** A receptor may be
reachable by more than one ligand, and the ligand's chemical class already has a
slot.

## Dosing interval lives on `Treatment`, not here

`dosing_interval` / `dosing_interval_days` apply to any treatment, so they stay
where they were. They are worth reading next to a `delivery_system`, because the
carrier is usually *why* the interval is what it is — vutrisiran's quarterly
subcutaneous dose against patisiran's three-weekly infusion with premedication is
a difference in carrier, not in mechanism or target.

## Two homes, for now

`oligonucleotide_details.delivery_platform` and
`oligonucleotide_details.conjugation` are still valid. They were kept rather than
removed for the reason recorded in
[Retired Enum Values](https://github.com/monarch-initiative/dismech/issues/10061):
retiring a spelling invalidates every PR already in flight that uses it, and
~44 oligonucleotide entries carry these slots. `conjugation` is marked deprecated
in favour of `targeting_ligand`; both render.

So two spellings are legal, and `just check-delivery-system` is what stops them
drifting:

```bash
just check-delivery-system                 # gate (runs in `just qc`)
just check-delivery-system --format list   # the full census, including the worklist
just check-delivery-system --strict        # also gate on the redundant case
```

It gates on three things, each a real defect:

- **`CONFLICT`** — the same fact in both places with *different* values. One is
  wrong and nothing downstream can tell which; the renderer resolves
  `delivery_system` first, so the nested value is hidden rather than surfaced.
- **`EMPTY`** — a `delivery_system` carrying no carrier fact. It renders as
  nothing; its absence says the same thing more honestly.
- **`LIGANDLESS_TARGET`** — a receptor named alongside
  `targeting_ligand: UNCONJUGATED`.

It reports, and does not gate on:

- **`DUPLICATE`** — the same fact in both places with the same value. Harmless
  today, one edit from a `CONFLICT`.
- **`LEGACY`** — the carrier recorded only in the nested block. This is the
  migration worklist and currently holds 81 findings. Gating on it would turn
  every oligonucleotide entry in the KB red for a change none of their curators
  made.

**New treatments — oligonucleotide or not — use `delivery_system`.** Only
`ATTR_Amyloidosis`'s vutrisiran has been migrated, as the worked targeted
example; the rest of the oligonucleotide corpus is deliberately left on the
nested spelling.

## Worked examples

| Entry | Treatment | What it demonstrates |
|---|---|---|
| `ATTR_Amyloidosis` | Vutrisiran | All four slots: `CONJUGATE` + `GALNAC` + ASGR1 + hepatocyte, migrated off the nested spelling |
| `Pancreatic_Ductal_Adenocarcinoma` | NALIRIFOX | `LIPOSOME` on a regimen where only one component is carried, with evidence |
| `Perivascular_Epithelioid_Cell_Neoplasm` | Nab-Sirolimus | `PROTEIN_NANOPARTICLE`, and a `notes:` recording why a hypothesized uptake route is not recorded as targeting |

`INORGANIC_NANOPARTICLE` has no worked example yet.

### The case that motivated the change

An antibody-coated mRNA lipid nanoparticle is the shape that the old schema
could not express at any point: the modality has no `oligonucleotide_details`
block to hang a carrier on, the ligand is coupled to the particle rather than to
the payload, and the whole therapeutic claim is *which cell it reaches*. Chen
et al. (*Sci Adv* 2026, [10.1126/sciadv.aed9568](https://doi.org/10.1126/sciadv.aed9568))
coat an mRNA-LNP with an anti-TREM2 antibody to reach tumor-associated
macrophages rather than the tumor cells beside them, reporting a
macrophage-to-tumour-cell uptake ratio of 5.1. In `delivery_system` that is:

```yaml
  therapeutic_modality: MRNA_THERAPY
  delivery_system:
    delivery_platform: LIPID_NANOPARTICLE
    targeting_ligand: ANTIBODY
    targeting_receptor:
      preferred_term: TREM2
    target_cell_types:
    - preferred_term: tumor-associated macrophage
```

This snippet is **illustrative only** — the agent is preclinical and no KB entry
curates it. It is here because it is the clearest statement of what the block is
for: the mechanism claim of a targeted nanomedicine is a claim about the
delivery system, not about the drug.
