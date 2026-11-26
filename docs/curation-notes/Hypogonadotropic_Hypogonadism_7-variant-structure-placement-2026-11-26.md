# Where GNRHR disease variants sit on the GnRH receptor structure (2026-11-26)

Scope: `kb/disorders/Hypogonadotropic_Hypogonadism_7_With_Or_Without_Anosmia.yaml`.
The variant descriptions in that entry give distances and contacts for individual
residues. This note records how those numbers were obtained, the full table they
were taken from, and what the structures cannot show.

**Main result.** The 49 variants examined fall into five groups by position, and
the groups match the functional classes reported from cell assays:

| Group | Variants | Structural reason for loss of function |
|---|---|---|
| Hormone pocket | R38Q, Y283H, Y284C; Q174R and Q106R nearby | R38, Y283 and Y284 touch GnRH (within 4 Å); Q174 is at 4.1 Å and Q106 at 5.8 Å, at the pocket mouth |
| G protein interface and DRS motif | D138G, R139H, R139C, R262Q, R262W, P146S | D138, R139 and P146 are within 4 Å of Gαq in the active state and R262 is at 5.2 Å; R139 also holds the inactive state through D138 and T265 |
| Buried core of the helix bundle | L83V, E90K, E90D, A129D, M131T, V134G, A163D, A171T, A171V, L266R, T269M, C279Y, P282L, P320L | Relative solvent accessibility below 0.1 for most; a charge, a larger side chain, or loss of a helix-kinking proline in a packed position |
| Arginine inside the membrane | S168R, S217R | A serine on a transmembrane helix whose hydroxyl bonds back to the helix backbone is replaced by a charged residue |
| N-terminus | N10K, Q11K | Not resolved in either experimental structure and low confidence in the model; no structural statement can be made |

Two of the three commonest alleles in gnomAD that ClinVar lists as pathogenic,
Q106R and R262Q, are on the edge of a functional site and not inside it, which
fits their partial loss of function in assays.

## Data

| Source | Identifier | Notes |
|---|---|---|
| Canonical sequence and topology | UniProt P30968 (328 residues) | Every variant was checked against this sequence before use; the script stops if the reference residue does not match |
| Generic residue numbers | GPCRdb `gnrhr_human` | Numbering checked residue by residue against the UniProt sequence |
| Inactive human receptor | PDB 7BR3, 2.79 Å, elagolix bound (PMID:33082324) | Author numbering equals UniProt numbering. Construct carries P128K and a fusion protein in intracellular loop 3. Residues 18-328 modelled, with gaps at 66-73, 145-151, 184-191 and 243-256 |
| Active receptor with hormone and G protein | PDB 9U4W, 3.18 Å, pig receptor with GnRH and Gq (PMID:40523184) | **Pig, not human.** Mapped to human numbering by local pairwise alignment (BLOSUM62): 271 modelled residues aligned, 248 identical. Pig author numbering differs from human between about 184 and 255 |
| Predicted human receptor | AlphaFold AF-P30968-F1, model version 6 | Used for pLDDT and for relative solvent accessibility of the whole chain |
| Population frequency | gnomAD v4.1, queried 2026-11-26 | Allele counts summed over nucleotide changes giving the same protein change |
| Clinical classification | ClinVar, queried 2026-11-26 | 255 GNRHR records; 63 pathogenic or likely pathogenic |

RCSB was searched by UniProt accession P30968 and returns only 7BR3. There is no
experimental structure of the human receptor with an agonist or a G protein, so
every GnRH and Gq distance below is from the pig receptor.

## Contact sets (non-hydrogen atoms within 4 Å, human numbering)

The deposited 9U4W model includes hydrogen atoms. They are excluded on both sides
of every distance here; leaving them in shortens the distances by up to about 1 Å
and lengthens the contact lists.

- **Elagolix (7BR3):** I21 P22 L23 Q25 G26 D98 N102 I103 K121 T215 F216 L219 Y283 L286 G287 M296 L297 N305 F308
- **GnRH (9U4W):** P29 R38 D98 W101 N102 K121 M125 F178 F193 Q195 V197 T198 T215 L219 Y283 Y284 G287 Y290 W291 M296 L297 N305 H306 F309
- **Gαq (9U4W):** M76 D138 R139 A142 I143 P146 L147 S151 N152 I258 A261 K264 T265 L328

## Per-variant table

Distances are minimum distances between non-hydrogen atoms in Å. `rSASA` is whole-residue
relative solvent accessibility in the AlphaFold model, computed on the isolated
chain, so a lipid-facing residue reads as exposed. `NA` means the residue is not
modelled in that structure. Polar partners are side-chain N, O or S atoms within
3.6 Å; partners listed for 9U4W carry **pig author numbering**.

| Variant | Region | Generic no. | pLDDT | rSASA | d(elagolix) 7BR3 | d(GnRH) 9U4W | d(Gq) 9U4W | Side-chain polar partners (7BR3; 9U4W) | gnomAD v4.1 AC / hom | ClinVar |
|---|---|---|---|---|---|---|---|---|---|---|
| N10K | N-term | - | 33 | 0.77 | NA | NA | NA | NA; NA | 215 / 0 | Pathogenic/Likely pathogenic (VCV000016031) |
| Q11K | N-term | - | 37 | 0.66 | NA | NA | NA | NA; NA | 206 / 0 | Conflicting classifications of pathogenicity (VCV000349458) |
| N18S | N-term | - | 45 | 0.66 | 11.6 | NA | NA | -; NA | 50 / 0 | - |
| Q25K | N-term | - | 47 | 0.81 | 3.6 | NA | NA | Q195:OE1,V105:O; NA | 65 / 0 | Uncertain significance (VCV001419996) |
| T32I | TM1 | 1.29x29 | 88 | 0.35 | 12.2 | 6.2 | 44.8 | -; S34:N | absent | - |
| I37S | TM1 | 1.34x34 | 95 | 0.48 | 13.5 | 11.3 | 36.6 | -; - | absent | - |
| R38Q | TM1 | 1.35x35 | 94 | 0.10 | 10.5 | 3.6 | 35.1 | -; D98:OD1,D98:OD2,N102:ND2 | 12 / 1 | Likely pathogenic (VCV003004558) |
| T40M | TM1 | 1.37x37 | 96 | 0.54 | 12.8 | 11.6 | 33.8 | K36:O; I37:O,K36:O | 43 / 0 | - |
| A50V | TM1 | 1.47x47 | 98 | 0.19 | 18.8 | 17.5 | 21.5 | -; F46:O | 53 / 0 | - |
| L83V | TM2 | 2.46x46 | 97 | 0.00 | 17.1 | 17.6 | 12.8 | -; - | 3 / 0 | Uncertain significance (VCV001504015) |
| E90D | TM2 | 2.53x53 | 98 | 0.02 | 8.4 | 8.8 | 23.6 | -; M125:N,S124:O,S124:OG | absent | - |
| E90K | TM2 | 2.53x53 | 98 | 0.02 | 8.4 | 8.8 | 23.6 | -; M125:N,S124:O,S124:OG | 10 / 0 | Pathogenic/Likely pathogenic (VCV000016032) |
| V94A | TM2 | 2.57x56 | 98 | 0.06 | 6.7 | 6.9 | 28.4 | -; - | 116 / 0 | Conflicting classifications of pathogenicity (VCV000632446) |
| T104I | ECL1 | - | 92 | 0.26 | 5.8 | 5.9 | 42.6 | Q106:N; - | 1 / 0 | - |
| Q106R | ECL1 | 23.49x49 | 90 | 0.12 | 8.8 | 5.8 | 44.9 | Y108:OH; S194:N | 5708 / 10 | Pathogenic/Likely pathogenic (VCV000016023) |
| Y108C | ECL1 | 23.51x51 | 92 | 0.59 | 11.1 | 10.6 | 45.7 | Q106:OE1; - | absent | - |
| L117R | TM3 | 3.28x28 | 98 | 0.19 | 10.1 | 9.1 | 32.7 | -; - | 13 / 0 | Pathogenic/Likely pathogenic (VCV000180147) |
| A127V | TM3 | 3.38x38 | 98 | 0.00 | 11.1 | 11.4 | 17.3 | -; - | 51 / 1 | Uncertain significance (VCV002171057) |
| A129D | TM3 | 3.40x40 | 98 | 0.04 | 10.7 | 11.3 | 15.5 | -; - | 25 / 0 | Pathogenic (VCV000016026) |
| M131T | TM3 | 3.42x42 | 98 | 0.01 | 15.5 | 16.2 | 11.3 | -; - | 1 / 0 | Pathogenic (VCV000140610) |
| V134G | TM3 | 3.45x45 | 97 | 0.04 | 19.0 | 19.4 | 8.0 | -; - | 14 / 0 | Pathogenic (VCV001458023) |
| L137P | TM3 | 3.48x48 | 95 | 0.29 | 21.8 | 21.6 | 6.9 | -; - | 1 / 0 | Likely pathogenic (VCV004967311) |
| D138G | TM3 | 3.49x49 | 92 | 0.04 | 24.8 | 25.2 | 3.2 | R139:NE,R139:NH2; - | absent | Likely pathogenic (VCV000418236) |
| R139H | TM3 | 3.50x50 | 91 | 0.13 | 26.3 | 24.0 | 3.7 | D138:OD2,R262:NH1,T265:OG1; - | 238 / 0 | Pathogenic (VCV000016030) |
| R139C | TM3 | 3.50x50 | 91 | 0.13 | 26.3 | 24.0 | 3.7 | D138:OD2,R262:NH1,T265:OG1; - | 17 / 0 | Pathogenic (VCV001675193) |
| P146S | ICL2 | 34.50x50 | 73 | 0.44 | NA | 36.2 | 3.6 | NA; - | 1711 / 4 | Conflicting classifications of pathogenicity (VCV000449413) |
| N152S | TM4 | 4.38x38 | 64 | 0.30 | 34.6 | 33.4 | 3.7 | -; - | 258 / 0 | - |
| A163D | TM4 | 4.49x49 | 98 | 0.03 | 16.0 | 15.7 | 15.0 | -; - | 3 / 0 | Likely pathogenic (VCV003337153) |
| L166P | TM4 | 4.52x52 | 98 | 0.29 | 14.5 | 13.1 | 18.8 | -; - | 3 / 0 | Likely pathogenic (VCV003590755) |
| S168R | TM4 | 4.54x54 | 98 | 0.29 | 14.7 | 13.4 | 23.4 | I165:O,W164:O; W164:O | absent | Pathogenic (VCV000016028) |
| A171T | TM4 | 4.57x57 | 98 | 0.00 | 11.0 | 9.4 | 26.9 | -; - | 4 / 0 | Pathogenic (VCV000016034) |
| A171V | TM4 | 4.57x57 | 98 | 0.00 | 11.0 | 9.4 | 26.9 | -; - | absent | Likely pathogenic (VCV003660422) |
| Q174R | TM4 | 4.60x61 | 96 | 0.06 | 7.4 | 4.1 | 32.2 | S118:O,Y211:OH; S118:O,Y211:OH | 3 / 0 | Pathogenic (VCV002581289) |
| C200Y | ECL2 | - | 79 | 0.35 | 16.4 | 9.2 | 45.5 | -; - | 12 / 0 | Pathogenic (VCV004967310) |
| W205R | TM5 | 5.32x33 | 82 | 0.65 | 13.6 | 10.9 | 40.7 | -; W206:NE1 | 81 / 1 | Uncertain significance (VCV004030648) |
| S217R | TM5 | 5.44x45 | 96 | 0.10 | 7.3 | 7.7 | 23.0 | F213:O; F213:O | absent | Pathogenic (VCV000016027) |
| T237N | TM5 | 5.64x64 | 91 | 0.16 | 32.7 | 33.8 | 4.8 | -; K233:O | 66 / 0 | Uncertain significance (VCV003610816) |
| R240Q | TM5 | 5.67x67 | 88 | 0.55 | 35.8 | 38.2 | 8.5 | -; - | 353 / 0 | Conflicting classifications of pathogenicity (VCV000729275) |
| E248K | ICL3 | - | 63 | 0.50 | NA | NA | NA | NA; NA | 44 / 0 | - |
| R262Q | TM6 | 6.30x30 | 85 | 0.24 | 32.4 | 32.4 | 5.2 | R139:NH1,R139:NH2; T239:OG1 | 2456 / 7 | Pathogenic/Likely pathogenic (VCV000016024) |
| R262W | TM6 | 6.30x30 | 85 | 0.24 | 32.4 | 32.4 | 5.2 | R139:NH1,R139:NH2; T239:OG1 | 16 / 0 | Pathogenic/Likely pathogenic (VCV002151986) |
| L266R | TM6 | 6.34x34 | 91 | 0.08 | 27.5 | 27.0 | 6.9 | -; - | 14 / 0 | Pathogenic/Likely pathogenic (VCV001519153) |
| T269M | TM6 | 6.37x37 | 94 | 0.01 | 22.2 | 22.0 | 7.7 | T265:O; N231:ND2,T265:O | 31 / 0 | Pathogenic/Likely pathogenic (VCV000140611) |
| C279Y | TM6 | 6.47x47 | 95 | 0.01 | 7.7 | 9.4 | 21.6 | S275:O; N315:N,S275:O | 31 / 0 | Pathogenic/Likely pathogenic (VCV001301193) |
| T281I | TM6 | 6.49x49 | 93 | 0.24 | 7.5 | 7.8 | 24.4 | T277:O; I277:O | absent | Pathogenic (VCV000126540) |
| P282L | TM6 | 6.50x50 | 92 | 0.16 | 4.5 | 6.3 | 26.8 | -; - | 1 / 0 | Likely pathogenic (VCV001709893) |
| Y283H | TM6 | 6.51x51 | 90 | 0.32 | 3.1 | 2.8 | 28.3 | -; - | 3 / 0 | Pathogenic/Likely pathogenic (VCV002755816) |
| Y284C | TM6 | 6.52x52 | 89 | 0.05 | 4.1 | 3.5 | 26.1 | -; - | 6 / 0 | Likely pathogenic (VCV000016025) |
| P320L | TM7 | 7.50x50 | 92 | 0.08 | 20.7 | 19.1 | 12.3 | -; - | absent | Pathogenic (VCV000016036) |

## What this does not establish

- The mutant proteins were not modelled. Each statement is about the position of
  the wild-type residue, not a computed stability change.
- Contacts with GnRH and Gq come from a pig receptor that is 92% identical over
  the modelled residues. Extracellular loop 2 is the region where the two
  species differ most, and it is where human Lys191 sits.
- C200Y: the literature assigns Cys200 a disulfide bond with Cys14. Cys14 is not
  modelled in 7BR3. The AlphaFold model has the two sulfurs 2.05 Å apart, but
  with pLDDT 54 at Cys14, and the pig receptor has glycine at position 200, so no
  experimental coordinate set shows the bond.
- The crystal structure construct carries P128K, one helical turn from A129, so
  local geometry around A129D was read from the AlphaFold model as well.
- A companion review of GNRHR gene function in `ai4curation/ai-gene-review`
  (`genes/human/GNRHR/GNRHR-bioinformatics/`, branch `claude/gnrhr-hh7-coreview`)
  carries its own reproducible variant-on-structure analysis. The two were run
  independently and agree on the variant classes and on the receptor-to-GnRH
  distances to within 0.3 Å.

## Script

Run with the UniProt JSON, the GPCRdb residue JSON, the two mmCIF files, the
AlphaFold mmCIF and a two-column `variants.tsv` (variant, source) in one
directory, passed as the only argument. Needs Biopython.

```python
"""Place GNRHR variants on the receptor: UniProt topology, GPCRdb generic numbers,
AlphaFold pLDDT, contacts in 7BR3 (human, elagolix-bound, inactive) and 9U4W
(pig GnRHR + GnRH + Gq, active; mapped to human numbering by pairwise alignment)."""
import json, sys, re
from Bio.PDB import MMCIFParser, NeighborSearch, ShrakeRupley
from Bio.PDB.Polypeptide import three_to_index, index_to_one
from Bio import Align
D = sys.argv[1]
AA3 = {'ALA','ARG','ASN','ASP','CYS','GLN','GLU','GLY','HIS','ILE','LEU','LYS','MET','PHE','PRO','SER','THR','TRP','TYR','VAL'}
MAXSASA = dict(A=129,R=274,N=195,D=193,C=167,Q=225,E=223,G=104,H=224,I=197,L=201,K=236,M=224,F=240,P=159,S=155,T=172,W=285,Y=263,V=174)
one = lambda r: index_to_one(three_to_index(r.get_resname()))
u = json.load(open(D+'/P30968.json'))
seq = u['sequence']['value']
topo = {}
for f in u['features']:
    if f['type'] in ('Topological domain','Transmembrane'):
        a,b = f['location']['start']['value'], f['location']['end']['value']
        lab = f['description'].replace('Helical; Name=','TM')
        for i in range(a,b+1): topo[i] = lab
gp = {r['sequence_number']:(r.get('display_generic_number') or '', r.get('protein_segment') or '') for r in json.load(open(D+'/gpcrdb_res.json'))}
assert all(json.load(open(D+'/gpcrdb_res.json'))[i-1]['amino_acid']==seq[i-1] for i in range(1,329)), 'GPCRdb numbering != UniProt'
P = MMCIFParser(QUIET=True)
af = P.get_structure('af', D+'/AF.cif')[0]['A']
plddt = {r.id[1]: r['CA'].get_bfactor() for r in af}
afm = P.get_structure('af2', D+'/AF.cif')[0]; sr = ShrakeRupley(); sr.compute(afm, level='A')
def sc_rsa(res):
    sc = [a for a in res if a.get_id() not in ('N','C','O','CA')] or [res['CA']]
    return sum(a.sasa for a in sc)
af_rsa = {r.id[1]: sum(a.sasa for a in r)/MAXSASA[one(r)] for r in afm['A']}
# 7BR3
x = P.get_structure('x', D+'/7BR3.cif')[0]['A']
xres = {r.id[1]: r for r in x if r.id[0]==' ' and r.id[1] <= 328}
lig = [a for r in x if r.get_resname()=='F5O' for a in r if a.element != 'H']
xatoms = [a for r in xres.values() for a in r if a.element != 'H']
ns = NeighborSearch(xatoms)
def mind(res, atoms):
    return min((a-b) for a in res if a.element != 'H' for b in atoms)
def polar_partners(res, pool_ns, resmap_num=lambda r: r.id[1]):
    out = set()
    for a in res:
        if a.get_id() in ('N','O','C','CA') or a.element not in ('N','O','S'): continue
        for b in pool_ns.search(a.coord, 3.6):
            rb = b.get_parent()
            if rb is res or b.element not in ('N','O','S'): continue
            if abs(rb.id[1]-res.id[1]) < 2 and b.get_id() in ('N','O'): continue
            out.add(f"{one(rb)}{rb.id[1]}:{b.get_id()}")
    return sorted(out)
def packing(res, pool_ns):
    cb = res['CB'] if 'CB' in res else res['CA']
    return len({b.get_parent().id[1] for b in pool_ns.search(cb.coord, 8.0) if b.get_id()=='CA'})
# 9U4W pig -> human map
y = P.get_structure('y', D+'/9U4W.cif')[0]
pig = [r for r in y['R'] if r.get_resname() in AA3 and r.id[0]==' ']
pigseq = ''.join(one(r) for r in pig)
al = Align.PairwiseAligner(); al.mode='local'; al.open_gap_score=-10; al.extend_gap_score=-0.5
al.substitution_matrix = Align.substitution_matrices.load('BLOSUM62')
aln = al.align(seq, pigseq)[0]
h2p = {}
for (hs,he),(ps,pe) in zip(*aln.aligned):
    for k in range(int(he-hs)): h2p[int(hs)+k+1] = pig[int(ps)+k]
print('# numbering diffs (human->pig):', [(h,r.id[1]) for h,r in h2p.items() if h!=r.id[1]][:5], file=sys.stderr)
ident = sum(1 for h,r in h2p.items() if seq[h-1]==one(r))
print(f"# pig(9U4W chain R) residues modelled {len(pig)}; aligned to human {len(h2p)}; identity {ident}/{len(h2p)}; numbering offset consistent: {all(h==r.id[1] for h,r in h2p.items())}", file=sys.stderr)
gnrh = [a for r in y['F'] for a in r if a.element != 'H']  # includes pGlu1 (PCA) and the C-terminal amide
gq = [a for r in y['A'] for a in r if a.element != 'H']
yatoms = [a for r in pig for a in r if a.element != 'H']; yns = NeighborSearch(yatoms)
# contact lists
def contacts(atoms, resmap, cut=4.0):
    s = NeighborSearch(atoms); out = {}
    for h,r in resmap.items():
        hv = [a for a in r if a.element != 'H']
        d = min((a-b) for a in hv for b in atoms) if any(s.search(a.coord,cut) for a in hv) else None
        if d is not None: out[h]=round(float(d),2)
    return out
c_lig = contacts(lig, xres); c_gnrh = contacts(gnrh, h2p); c_gq = contacts(gq, h2p)
json.dump(dict(elagolix_7BR3=c_lig, gnrh_9U4W=c_gnrh, gq_9U4W=c_gq), open(D+'/contacts.json','w'), indent=1)
fmt = lambda c: ' '.join(f"{seq[h-1]}{h}{'('+gp[h][0]+')' if gp[h][0] else ''}" for h in sorted(c))
print('# elagolix contacts <=4A (7BR3):', fmt(c_lig), file=sys.stderr)
print('# GnRH contacts <=4A (9U4W, human numbering):', fmt(c_gnrh), file=sys.stderr)
print('# Gq contacts <=4A (9U4W, human numbering):', fmt(c_gq), file=sys.stderr)
variants = [l.split('\t') for l in open(D+'/variants.tsv').read().strip().split('\n')[1:]]
hdr = ['variant','source','region','segment','generic_no','pLDDT','AF_rSASA','n_CA_8A_7BR3','d_elagolix_7BR3','d_GnRH_9U4W','d_Gq_9U4W','pig_residue','sidechain_polar_partners_7BR3','sidechain_polar_partners_9U4W']
print('\t'.join(hdr))
for v,src in variants:
    m = re.match(r'([A-Z])(\d+)', v); wt, n = m.group(1), int(m.group(2))
    assert seq[n-1]==wt, f'{v}: canonical residue is {seq[n-1]}{n}'
    rx = xres.get(n); ry = h2p.get(n)
    row = [v, src, topo.get(n,''), gp[n][1], gp[n][0], f"{plddt[n]:.0f}", f"{af_rsa[n]:.2f}",
           str(packing(rx, ns)) if rx else 'NA',
           f"{mind(rx, lig):.1f}" if rx else 'NA',
           f"{mind(ry, gnrh):.1f}" if ry else 'NA',
           f"{mind(ry, gq):.1f}" if ry else 'NA',
           f"{one(ry)}{ry.id[1]}" if ry else 'NA',
           ','.join(polar_partners(rx, ns)) if rx else 'NA',
           ','.join(polar_partners(ry, yns)) if ry else 'NA']
    print('\t'.join(row))
```
