## Issue

Enhance the phenotype section for `kb/disorders/Atelosteogenesis_Type_I.yaml`
without broadening into a full-page rewrite.

## PMID-backed phenotype evidence used

- `PMID:24624349`
  - Abstract support: severe short-limbed dwarfism; dislocated hips, knees, and elbows.
  - YAML use: `Disproportionate Short-Limb Short Stature`, `Joint Dislocation`.

- `PMID:23401428`
  - Abstract support: severe rhizomelic shortening of the extremities, pectus excavatum, broad thumbs, brachydactyly, dislocated hips, bilateral talipes equinovarus.
  - Abstract support: facial features included proptosis, hypertelorism, downslanting palpebral fissures, cleft palate, and retromicrognathia.
  - YAML use: `Rhizomelia`, `Talipes Equinovarus`, `Brachydactyly`, `Broad Thumb`, `Pectus Excavatum`, `Proptosis`, `Hypertelorism`, `Downslanting Palpebral Fissures`, `Micrognathia`, `Cleft Palate`.

- `PMID:16752402`
  - Abstract support: vertebral abnormalities, disharmonious skeletal maturation, hypoplastic long bones, and joint dislocations in AOI/AOIII.
  - YAML use: retained vertebral phenotype support and kept the phenotype block grounded in a multi-patient FLNB series rather than single-case reports alone.

- `PMID:12454961`
  - Abstract support: absent or deficient ossification of the posterior neural arches of the thoracic spine, humeri, radii, ulnae, fibulae, and short tubular bones; extremely short, thick femora; pulmonary hypoplasia; laryngeal stenosis; large cisterna magna.
  - YAML use: strengthened `Abnormality of the Vertebral Column`, retained `Fibular Aplasia`, retained `Pulmonary Hypoplasia`.

- `PMID:9779808`
  - Abstract support: incomplete ossification of cartilage anlagen; pulmonary hypoplasia as a characteristic finding; severe subglottic hypoplasia and tracheomalacia.
  - YAML use: added recurrent support for `Pulmonary Hypoplasia`; added `Tracheomalacia`.

## Claims intentionally not added as standalone AOI phenotypes

- `Hitchhiker thumbs`, `midfacial flattening`, `renal microcysts`, `abnormal pancreatic duct branching`, `caecal malrotation`, and `retinal dysplasia` were left out because the support was isolated to small autopsy series or appeared as overlap findings rather than clearly grounded core AOI manifestations for this issue.

- `Large cisterna magna` was not added because it is currently supported by a single prenatal case report and did not appear strong enough to elevate into the main AOI phenotype block for this focused curation pass.

- Airway narrowing terms more specific than `Tracheomalacia` were not added in YAML because the abstract evidence was strongest for tracheomalacia, while laryngeal/subglottic narrowing language was less straightforward to ground to a single specific HPO term without risking ontology mismatch.

## Curation approach

- Prefer phenotype terms already used elsewhere in the repo when they fit the literature cleanly.
- Avoid adding `frequency` or structured `onset` because the AOI literature used here did not provide robust quantitative phenotype frequencies, and the phenotype evidence was mostly fetal/newborn case material rather than cohort-level onset summaries.
- Soften wording for single-series findings by describing them as reported or documented rather than universal hallmarks.
- Keep non-phenotype sections minimal in this issue-specific pass; treatment claims without direct treatment evidence were removed rather than supported indirectly with pathology snippets.
