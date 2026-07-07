#!/usr/bin/env python
"""Regenerate all five figures for the Iron-Related Ferroptosis Superimposition Model report.
Reads data_*.json / *.csv in this folder. Requires: pandas, matplotlib.
Run:  python make_figures.py
"""

import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

plt.rcParams.update({"font.size": 8, "axes.titlesize": 8, "figure.dpi": 300})
HERE = __import__("os").path.dirname(__file__) or "."


def p(f):
    return f"{HERE}/{f}"


# ---------- Fig 1: evidence chain heatmap ----------
ext = pd.read_csv(p("data_evidence_matrix.csv")).fillna("")
LINKS = [
    "L1_cu_primary",
    "L2_secondary_iron",
    "L3_cp_ferroxidase",
    "L4_iron_ferroptosis",
    "L5_wd_ferroptosis",
    "L6_cu_fe_crosstalk",
]
LABELS = [
    "L1 Copper is the\nprimary lesion",
    "L2 Secondary iron\noverload (subset)",
    "L3 Ceruloplasmin\nferroxidase \u2192 Fe export",
    "L4 Iron \u2192 ferroptosis\n(lipid peroxidation)",
    "L5 Ferroptosis in\nWD models/patients",
    "L6 Copper\u2013iron /\ncupro\u2013ferroptosis crosstalk",
]
levels = ["STRONG", "PARTIAL", "MENTION"]
mat = np.array([[(ext[k + "_s"] == lv).sum() for lv in levels] for k in LINKS], float)
fig, ax = plt.subplots(figsize=(7.2, 4.6))
im = ax.imshow(mat, cmap=plt.cm.Blues, aspect="auto", vmin=0, vmax=mat.max())
ax.set_xticks(range(3))
ax.set_xticklabels(["Strong", "Partial", "Mention"])
ax.set_yticks(range(6))
ax.set_yticklabels(LABELS)
for i in range(6):
    for j in range(3):
        v = int(mat[i, j])
        ax.text(
            j,
            i,
            str(v),
            ha="center",
            va="center",
            color="white" if v > mat.max() * 0.55 else "#1a1a1a",
            fontweight="bold",
        )
ax.set_title(
    "Literature support for each link of the ferroptosis-superimposition chain\n(n=102 abstracts classified; 0 contradictions across all links)"
)
ax.set_xlabel("Strength of evidence in abstract  (Strong \u2192 Mention)")
cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
cb.set_label("Papers")
fig.tight_layout()
fig.savefig(p("fig1_evidence_chain.png"), dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------- Fig 2: mechanism bridge ----------
net = json.load(open(p("data_string_network.json")))
pos = {
    "ATP7B": (0.06, 0.72),
    "CP": (0.33, 0.72),
    "HEPH": (0.33, 0.40),
    "SLC40A1": (0.60, 0.55),
    "TFRC": (0.60, 0.86),
    "FTH1": (0.78, 0.72),
    "STEAP3": (0.60, 0.24),
    "GPX4": (0.92, 0.45),
    "ACSL4": (0.92, 0.20),
    "SLC7A11": (0.78, 0.28),
}
grp = {
    "ATP7B": "cu",
    "CP": "bridge",
    "HEPH": "bridge",
    "SLC40A1": "fe",
    "TFRC": "fe",
    "FTH1": "fe",
    "STEAP3": "fe",
    "GPX4": "fp",
    "ACSL4": "fp",
    "SLC7A11": "fp",
}
col = {"cu": "#c56c00", "bridge": "#7a3b8f", "fe": "#1f6feb", "fp": "#c0341d"}
sub = {"SLC40A1": "ferroportin", "CP": "ceruloplasmin"}
fig, ax = plt.subplots(figsize=(8.4, 4.8))
ax.axis("off")
for e in net["edges"]:
    a, b, s = e["a"], e["b"], e["score"]
    if a in pos and b in pos:
        ax.plot(
            [pos[a][0], pos[b][0]],
            [pos[a][1], pos[b][1]],
            color="#b8b8b8",
            lw=0.6 + 2.6 * (s - 0.7) / 0.3,
            zorder=1,
        )
for g, (x, y) in pos.items():
    ax.scatter(
        [x],
        [y],
        s=1500,
        color=col[grp[g]],
        alpha=0.92,
        zorder=3,
        edgecolors="white",
        linewidths=1.2,
    )
    ax.text(
        x,
        y + (0.012 if g in sub else 0),
        g,
        ha="center",
        va="center",
        color="white",
        fontsize=6.8,
        fontweight="bold",
        zorder=4,
    )
    if g in sub:
        ax.text(
            x,
            y - 0.032,
            sub[g],
            ha="center",
            va="center",
            color="white",
            fontsize=5.4,
            zorder=4,
        )
ax.scatter(
    [pos["CP"][0]],
    [pos["CP"][1]],
    s=2500,
    facecolors="none",
    edgecolors="#7a3b8f",
    linewidths=2.2,
    zorder=2,
)
ax.annotate(
    "Molecular bridge:\nCu-loaded ferroxidase\noxidises Fe\u00b2\u207a for export",
    xy=pos["CP"],
    xytext=(0.055, 0.44),
    ha="center",
    va="center",
    fontsize=6.4,
    color="#7a3b8f",
    fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="#7a3b8f", lw=1.1),
)
for lab, x, c in [
    ("Copper axis\n(WD primary lesion)", 0.06, "#c56c00"),
    ("Iron handling\n(export / storage / import)", 0.66, "#1f6feb"),
    ("Ferroptosis\neffectors", 0.92, "#c0341d"),
]:
    ax.text(
        x, 0.04, lab, ha="center", va="center", fontsize=6.8, color=c, fontweight="bold"
    )
ax.text(
    0.5,
    1.08,
    "Molecular route from copper toxicity to iron-driven ferroptosis",
    ha="center",
    fontsize=9,
    transform=ax.transAxes,
)
ax.text(
    0.5,
    1.02,
    "STRING v12 high-confidence edges (\u22650.70); ATP7B\u2013CP = 0.98, CP\u2013ferroportin = 0.98",
    ha="center",
    fontsize=6.6,
    color="#555",
    transform=ax.transAxes,
)
ax.set_xlim(-0.02, 1.02)
ax.set_ylim(0, 1)
fig.savefig(p("fig2_mechanism_bridge.png"), dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------- Fig 3: human cohort (Gromadzka 2021, PMID 33555495) ----------
markers = {
    "Ferritin (ng/mL)": [158.9, 77.0, 47.5],
    "Serum iron (\u00b5g/dL)": [126.0, 88.0, 103.5],
    "Hepcidin (ng/mL)": [32.6, 16.7, 12.1],
}
panels = ["Ferritin (ng/mL)", "Hepcidin (ng/mL)", "Serum iron (\u00b5g/dL)"]
colors = ["#c0341d", "#7a7a7a", "#1f6feb"]
groups = ["Untreated\nWD", "Treated\nWD", "Controls"]
fig, axes = plt.subplots(1, 3, figsize=(8.6, 3.2))
for ax, mk in zip(axes, panels):
    vals = markers[mk]
    x = np.arange(3)
    ax.bar(x, vals, color=colors, width=0.66, edgecolor="white")
    for xi, v in zip(x, vals):
        ax.text(
            xi,
            v,
            f"{v:.0f}" if v >= 10 else f"{v:.1f}",
            ha="center",
            va="bottom",
            fontsize=6.6,
            fontweight="bold",
        )
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.set_title(mk)
    ax.margins(y=0.16)
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylabel("Concentration")
fig.suptitle(
    "Iron metabolism is disturbed in untreated Wilson disease and improves \u2014 but is not normalised \u2014 by anti-copper therapy",
    fontsize=8.2,
    y=1.06,
)
fig.text(
    0.5,
    -0.06,
    "Human cohort, Gromadzka et al. 2021 (PMID 33555495). Untreated WD: ferritin & hepcidin elevated vs controls (p<0.001\u20130.005); serum ceruloplasmin 5.4 vs 31.8 mg/dL. Treatment lowers but does not restore control values.",
    ha="center",
    fontsize=6.2,
    color="#555",
)
fig.tight_layout()
fig.savefig(p("fig3_human_cohort.png"), dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------- Fig 4: sex-stratified subset (Gromadzka 2020, PMID 32937238) ----------
data = {
    "Ferritin (ng/mL)": {"Naive": (290.5, 81.0), "Treated": (122.0, 46.0)},
    "Hepcidin (ng/mL)": {"Naive": (55.4, 22.8), "Treated": (23.5, 10.8)},
    "Serum iron (\u00b5g/dL)": {"Naive": (None, None), "Treated": (102.5, 68.0)},
}
panels = list(data)
fig, axes = plt.subplots(1, 3, figsize=(8.8, 3.4))
male_c = "#1f5fb0"
female_c = "#d98a2b"
for ax, mk in zip(axes, panels):
    x = np.arange(2)
    w = 0.36
    g = ["Naive", "Treated"]
    m = [data[mk][k][0] for k in g]
    f = [data[mk][k][1] for k in g]
    ax.bar(
        x - w / 2, [v or 0 for v in m], w, color=male_c, label="Men", edgecolor="white"
    )
    ax.bar(
        x + w / 2,
        [v or 0 for v in f],
        w,
        color=female_c,
        label="Women",
        edgecolor="white",
    )
    for xi, v in zip(x - w / 2, m):
        ax.text(
            xi, v, f"{v:.0f}", ha="center", va="bottom", fontsize=6.2, fontweight="bold"
        ) if v is not None else ax.text(
            xi, 1, "n.s.", ha="center", va="bottom", fontsize=6, color="#888"
        )
    for xi, v in zip(x + w / 2, f):
        if v is not None:
            ax.text(
                xi,
                v,
                f"{v:.0f}",
                ha="center",
                va="bottom",
                fontsize=6.2,
                fontweight="bold",
            )
    ax.set_xticks(x)
    ax.set_xticklabels(["Treatment-\nnaive", "Treated"])
    ax.set_title(mk)
    ax.margins(y=0.18)
    ax.spines[["top", "right"]].set_visible(False)
axes[0].set_ylabel("Concentration")
axes[0].legend(frameon=False, fontsize=6.6, loc="upper right")
fig.suptitle(
    "The at-risk subset is sex-defined: men with Wilson disease carry a consistently higher iron burden",
    fontsize=8.4,
    y=1.06,
)
fig.text(
    0.5,
    -0.07,
    "Gromadzka et al. 2020 (PMID 32937238), n=138 (39 naive / 99 treated). Men > women for ferritin, hepcidin and (treated) serum iron, all p<0.05. Consistent with impaired CP-ferroxidase iron export unmasked where menstrual iron loss is absent.",
    ha="center",
    fontsize=6.1,
    color="#555",
)
fig.tight_layout()
fig.savefig(p("fig4_sex_subset.png"), dpi=300, bbox_inches="tight")
plt.close(fig)

# ---------- Fig 5: crosstalk network ----------
net = json.load(open(p("data_crosstalk_string.json")))
grp = {
    "FDX1": "cup",
    "LIAS": "cup",
    "DLAT": "cup",
    "LIPT1": "cup",
    "DLD": "cup",
    "GPX4": "fer",
    "SLC7A11": "fer",
    "ACSL4": "fer",
    "NFE2L2": "red",
    "GCLC": "red",
    "GSS": "red",
    "NQO1": "red",
    "ATP7B": "cu",
    "CP": "cu",
    "SLC40A1": "cu",
    "FTH1": "cu",
    "SLC31A1": "cu",
    "ISCU": "fes",
    "FXN": "fes",
}
col = {
    "cup": "#c56c00",
    "fer": "#c0341d",
    "red": "#2a9d5c",
    "cu": "#7a3b8f",
    "fes": "#1f6feb",
}
lab = {
    "cup": "Cuproptosis / lipoylation",
    "fer": "Ferroptosis effectors",
    "red": "Glutathione / NRF2 hub",
    "cu": "Metal transport",
    "fes": "Fe-S cluster biogenesis",
}
pos = {
    "FDX1": (0.14, 0.80),
    "LIAS": (0.06, 0.62),
    "DLAT": (0.20, 0.64),
    "LIPT1": (0.10, 0.46),
    "DLD": (0.24, 0.48),
    "ISCU": (0.34, 0.66),
    "FXN": (0.40, 0.50),
    "ATP7B": (0.30, 0.90),
    "CP": (0.48, 0.78),
    "SLC40A1": (0.60, 0.64),
    "FTH1": (0.70, 0.50),
    "SLC31A1": (0.40, 0.90),
    "NFE2L2": (0.66, 0.86),
    "GCLC": (0.74, 0.72),
    "GSS": (0.82, 0.60),
    "NQO1": (0.78, 0.88),
    "GPX4": (0.90, 0.68),
    "SLC7A11": (0.90, 0.86),
    "ACSL4": (0.96, 0.52),
}
fig, ax = plt.subplots(figsize=(9.2, 5.2))
ax.axis("off")
for e in net["edges"]:
    a, b, s = e["a"], e["b"], e["score"]
    if a in pos and b in pos:
        cross = grp.get(a) != grp.get(b)
        ax.plot(
            [pos[a][0], pos[b][0]],
            [pos[a][1], pos[b][1]],
            color=("#555" if cross else "#c8c8c8"),
            lw=0.5 + 2.4 * (s - 0.7) / 0.3,
            alpha=0.9 if cross else 0.6,
            zorder=1,
        )
for g, (x, y) in pos.items():
    ax.scatter(
        [x],
        [y],
        s=760,
        color=col[grp[g]],
        alpha=0.93,
        zorder=3,
        edgecolors="white",
        linewidths=1,
    )
    ax.text(
        x,
        y,
        g,
        ha="center",
        va="center",
        color="white",
        fontsize=5.6,
        fontweight="bold",
        zorder=4,
    )
ax.annotate(
    "Bridge 1 \u2014 metal transport:\nATP7B\u2192CP\u2192ferroportin",
    xy=(0.48, 0.78),
    xytext=(0.30, 0.30),
    fontsize=6.3,
    color="#7a3b8f",
    fontweight="bold",
    ha="center",
    arrowprops=dict(arrowstyle="->", color="#7a3b8f", lw=1),
)
ax.annotate(
    "Bridge 2 \u2014 Fe-S / redox:\nCu-driven loss of Fe-S (FDX1,LIAS,ISCU,FXN)\nconverges with GSH depletion on GPX4",
    xy=(0.74, 0.72),
    xytext=(0.52, 0.16),
    fontsize=6.3,
    color="#2a9d5c",
    fontweight="bold",
    ha="center",
    arrowprops=dict(arrowstyle="->", color="#2a9d5c", lw=1),
)
h = [
    Line2D(
        [0],
        [0],
        marker="o",
        color="w",
        markerfacecolor=col[k],
        markersize=8,
        label=lab[k],
    )
    for k in ["cu", "fes", "cup", "red", "fer"]
]
ax.legend(
    handles=h,
    frameon=False,
    fontsize=6.3,
    loc="upper left",
    bbox_to_anchor=(-0.02, 1.0),
)
ax.text(
    0.5,
    1.05,
    "Cuproptosis\u2013ferroptosis crosstalk: two molecular bridges couple copper toxicity to iron-driven cell death",
    ha="center",
    fontsize=8.6,
    transform=ax.transAxes,
)
ax.text(
    0.5,
    1.00,
    "STRING v12 edges \u22650.70; dark edges cross functional modules. Hubs by degree: GPX4(5), GCLC(4), CP/FXN/ISCU/NFE2L2(3).",
    ha="center",
    fontsize=6.2,
    color="#555",
    transform=ax.transAxes,
)
ax.set_xlim(0, 1)
ax.set_ylim(0.05, 1)
fig.savefig(p("fig5_crosstalk_network.png"), dpi=300, bbox_inches="tight")
plt.close(fig)
print("Regenerated 5 figures.")
