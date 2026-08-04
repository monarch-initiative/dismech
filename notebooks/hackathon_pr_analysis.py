# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "altair>=5.5.0",
#   "marimo>=0.14.0",
#   "pandas>=2.2.0",
# ]
# ///

import marimo

__generated_with = "0.23.16"
app = marimo.App(width="medium")


@app.cell
def _():
    import altair as alt
    import marimo as mo
    import pandas as pd

    return alt, mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # dismech hackathon PR analysis

    **Cohort:** all 597 pull requests opened in `monarch-initiative/dismech`
    from **2026-07-29 00:00 UTC** through **2026-08-03 22:53 UTC**.
    The local analysis branch was rebased to `origin/main` at `ea5c7a1000` before
    collection.

    ## Executive readout

    - **18 author accounts** opened PRs: **15 people** and **3 automation accounts**
      (`ai4c-agent`, `github-actions`, and `dependabot`). People authored 422 PRs;
      335 were merged at snapshot time.
    - The dominant work was curation: **226 PRs added 231 disorder files** and
      **192 PRs modified existing disorder files**. Ten PRs did both.
    - **223 PRs included deep-research artifacts**; 221 of those were human-authored.
      Thirteen of the 15 human contributors used deep research at least once.
    - The distinct **OpenScientist hypothesis-exploration workflow** was driven by
      **cmungall (32 PRs)**. This is separate from using OpenScientist as a
      deep-research provider for disease-entry curation (19 PRs across six people).
    - Review was intensive: human PRs averaged **2.52 formal AI review rounds**;
      34 had five or more. More rounds track with longer merge time, but the median
      remained hours, not days.
    - The work arrived as a **two-day production burst**: Friday and Saturday
      account for 307 of 422 human PRs (73%). Saturday alone produced 100
      new-entry PRs and 105 PRs with deep-research artifacts.
    - New entries were large but moved quickly (median 6,955 changed lines and
      2.92 hours to merge). Enhancements were much smaller (median 872 lines) yet
      took 12.28 hours to merge, pointing to branch age, shared-file conflicts,
      and review/rebase coordination—not raw diff size—as the larger bottleneck.
    - There is **one clear, explicit frustration episode** in the corpus: PR #7257.
      It describes five rounds/five approvals, diminishing returns from successive
      optional suggestions, and reviewer capability drift. That is real evidence of
      review-loop frustration, but not evidence that frustration was widespread.
    """)
    return


@app.cell
def _(pd):
    daily_mix = pd.DataFrame(
        [
            ("Jul 29", "New entry", 4),
            ("Jul 29", "Enhancement", 5),
            ("Jul 29", "New + enhancement", 1),
            ("Jul 29", "OpenScientist hypothesis", 4),
            ("Jul 29", "Review/audit", 1),
            ("Jul 29", "Tooling/other", 3),
            ("Jul 30", "New entry", 11),
            ("Jul 30", "Enhancement", 33),
            ("Jul 30", "New + enhancement", 1),
            ("Jul 30", "OpenScientist hypothesis", 0),
            ("Jul 30", "Review/audit", 1),
            ("Jul 30", "Tooling/other", 4),
            ("Jul 31", "New entry", 62),
            ("Jul 31", "Enhancement", 44),
            ("Jul 31", "New + enhancement", 4),
            ("Jul 31", "OpenScientist hypothesis", 25),
            ("Jul 31", "Review/audit", 2),
            ("Jul 31", "Tooling/other", 15),
            ("Aug 1", "New entry", 100),
            ("Aug 1", "Enhancement", 34),
            ("Aug 1", "New + enhancement", 3),
            ("Aug 1", "OpenScientist hypothesis", 0),
            ("Aug 1", "Review/audit", 3),
            ("Aug 1", "Tooling/other", 15),
            ("Aug 2", "New entry", 28),
            ("Aug 2", "Enhancement", 9),
            ("Aug 2", "New + enhancement", 1),
            ("Aug 2", "OpenScientist hypothesis", 0),
            ("Aug 2", "Review/audit", 1),
            ("Aug 2", "Tooling/other", 3),
            ("Aug 3*", "New entry", 1),
            ("Aug 3*", "Enhancement", 1),
            ("Aug 3*", "New + enhancement", 0),
            ("Aug 3*", "OpenScientist hypothesis", 0),
            ("Aug 3*", "Review/audit", 1),
            ("Aug 3*", "Tooling/other", 2),
        ],
        columns=["day", "contribution", "PRs"],
    )
    daily_summary = pd.DataFrame(
        [
            ("Jul 29", 18, 6, 5, 49, 497),
            ("Jul 30", 50, 8, 12, 151, 318),
            ("Jul 31", 152, 12, 73, 389, 3163),
            ("Aug 1", 155, 10, 105, 374, 6695),
            ("Aug 2", 42, 7, 26, 91, 6229),
            ("Aug 3*", 5, 3, 0, 9, 822),
        ],
        columns=[
            "day",
            "human PRs",
            "active authors",
            "deep-research PRs",
            "formal reviews",
            "median lines",
        ],
    )
    day_order = ["Jul 29", "Jul 30", "Jul 31", "Aug 1", "Aug 2", "Aug 3*"]
    return daily_mix, daily_summary, day_order


@app.cell(hide_code=True)
def _(alt, daily_mix, daily_summary, day_order, mo):
    throughput_bars = (
        alt.Chart(daily_mix)
        .mark_bar()
        .encode(
            x=alt.X("day:N", sort=day_order, title=None),
            y=alt.Y("PRs:Q", title="Human-authored PRs"),
            color=alt.Color("contribution:N", title="Primary contribution"),
            order=alt.Order("contribution:N"),
            tooltip=["day", "contribution", "PRs"],
        )
    )
    author_line = (
        alt.Chart(daily_summary)
        .mark_line(point=True)
        .encode(
            x=alt.X("day:N", sort=day_order),
            y=alt.Y(
                "active authors:Q",
                axis=alt.Axis(title="Active authors", orient="right"),
            ),
            tooltip=["day", "active authors", "formal reviews", "median lines"],
        )
    )
    throughput_chart = (
        alt.layer(throughput_bars, author_line)
        .resolve_scale(y="independent")
        .properties(
            width=760,
            height=300,
            title="The hackathon became a two-day production burst",
        )
    )
    mo.vstack(
        [
            mo.md("## Throughput over the hackathon"),
            throughput_chart,
            mo.md(
                """
                Friday and Saturday generated **307 human PRs—73% of the entire
                cohort**. The mode changed over the event: Thursday was enhancement-heavy;
                Friday mixed entry creation with the OpenScientist assessment sprint;
                Saturday became a new-entry factory, with 100 new-entry PRs and 105
                deep-research PRs. The `Aug 3*` bar is a partial day ending at 22:53 UTC.

                The burst was highly parallel rather than a single-user batch: 12 distinct
                human authors opened PRs on Friday and 10 on Saturday. That parallelism
                explains both the output and many of the later merge conflicts.
                """
            ),
        ]
    )
    return


@app.cell
def _(pd):
    account_summary = pd.DataFrame(
        [
            {
                "account class": "people",
                "accounts": 15,
                "PRs": 422,
                "merged": 335,
                "open": 81,
                "closed unmerged": 6,
            },
            {
                "account class": "automation",
                "accounts": 3,
                "PRs": 175,
                "merged": 32,
                "open": 50,
                "closed unmerged": 93,
            },
        ]
    )

    contribution_categories = pd.DataFrame(
        [
            ("new disorder entry", 216),
            ("existing-entry enhancement", 182),
            ("automation / generated output", 104),
            ("tooling, schema, or docs", 33),
            ("OpenScientist hypothesis workflow", 29),
            ("other", 11),
            ("new entry + enhancement", 10),
            ("review or audit", 9),
            ("mechanism module", 3),
        ],
        columns=["category", "PRs"],
    )
    return account_summary, contribution_categories


@app.cell(hide_code=True)
def _(account_summary, alt, contribution_categories, mo):
    category_chart = (
        alt.Chart(contribution_categories)
        .mark_bar()
        .encode(
            x=alt.X("PRs:Q", title="Pull requests"),
            y=alt.Y("category:N", sort="-x", title=None),
            tooltip=["category", "PRs"],
        )
        .properties(
            width=760,
            height=260,
            title="Primary contribution type (exclusive classification)",
        )
    )
    mo.vstack(
        [
            mo.md("## Volume and contribution types"),
            mo.ui.table(account_summary, selection=None, pagination=False),
            category_chart,
            mo.md(
                """
                The exclusive chart assigns each PR one primary class. The underlying
                multi-label counts are 226 new-entry PRs, 192 enhancement PRs, 223
                deep-research PRs, and 32 OpenScientist hypothesis-workflow PRs.
                Research is an input to curation, so it intentionally overlaps the entry
                categories rather than competing with them.
                """
            ),
        ]
    )
    return


@app.cell
def _(pd):
    contributors = pd.DataFrame(
        [
            ("cmungall", 106, 97, 7, 9, 58, 6, 1, 32, 254),
            ("kevinschaper", 74, 50, 69, 68, 7, 70, 0, 0, 182),
            ("jmcmurry", 58, 54, 44, 44, 13, 43, 0, 0, 133),
            ("mellybelly", 42, 18, 11, 17, 25, 11, 4, 0, 105),
            ("caufieldjh", 40, 37, 21, 21, 4, 21, 0, 0, 107),
            ("nlharris", 34, 33, 12, 15, 13, 12, 6, 0, 94),
            ("Phillip-a-richmond", 18, 15, 14, 14, 5, 16, 5, 0, 53),
            ("DnlRKorn", 12, 1, 10, 10, 2, 11, 0, 0, 12),
            ("bpow", 10, 9, 10, 10, 0, 10, 2, 0, 34),
            ("sierra-moxon", 10, 7, 8, 8, 1, 8, 0, 0, 40),
            ("tannerzhang", 8, 6, 6, 6, 2, 8, 0, 0, 23),
            ("oneilsh", 5, 5, 2, 2, 3, 3, 1, 0, 17),
            ("sabrinatoro", 3, 2, 1, 1, 2, 2, 0, 0, 7),
            ("flahartyka", 1, 0, 1, 1, 0, 0, 0, 0, 1),
            ("gingin77", 1, 1, 0, 0, 1, 0, 0, 0, 1),
        ],
        columns=[
            "author",
            "PRs",
            "merged",
            "new-entry PRs",
            "new disorder files",
            "enhancement PRs",
            "deep-research PRs",
            "OpenScientist DR PRs",
            "OpenScientist hypothesis PRs",
            "formal AI reviews",
        ],
    )
    return (contributors,)


@app.cell(hide_code=True)
def _(contributors, mo):
    mo.vstack(
        [
            mo.md("## Human contributors"),
            mo.ui.table(contributors, selection=None, page_size=15),
            mo.md(
                """
                Counts are by PR author, not by commenters or commit co-authors. “New”
                uses GitHub's file status (`added`), avoiding the common error of calling
                an append-only edit a new file. A PR may add more than one disorder.
                """
            ),
        ]
    )
    return


@app.cell
def _(pd):
    contributor_mix = pd.DataFrame(
        [
            ("cmungall", "OpenScientist hypothesis", 29),
            ("cmungall", "Enhancement", 55),
            ("cmungall", "New + enhancement", 3),
            ("cmungall", "New entry", 4),
            ("cmungall", "Review/audit", 3),
            ("cmungall", "Tooling/other", 12),
            ("kevinschaper", "Enhancement", 4),
            ("kevinschaper", "New + enhancement", 3),
            ("kevinschaper", "New entry", 66),
            ("kevinschaper", "Tooling/other", 1),
            ("jmcmurry", "Enhancement", 13),
            ("jmcmurry", "New entry", 44),
            ("jmcmurry", "Tooling/other", 1),
            ("mellybelly", "Enhancement", 24),
            ("mellybelly", "New + enhancement", 1),
            ("mellybelly", "New entry", 10),
            ("mellybelly", "Review/audit", 1),
            ("mellybelly", "Tooling/other", 6),
            ("caufieldjh", "Enhancement", 3),
            ("caufieldjh", "New + enhancement", 1),
            ("caufieldjh", "New entry", 20),
            ("caufieldjh", "Review/audit", 2),
            ("caufieldjh", "Tooling/other", 14),
            ("nlharris", "Enhancement", 13),
            ("nlharris", "New entry", 12),
            ("nlharris", "Review/audit", 3),
            ("nlharris", "Tooling/other", 6),
            ("Phillip-a-richmond", "Enhancement", 3),
            ("Phillip-a-richmond", "New + enhancement", 2),
            ("Phillip-a-richmond", "New entry", 12),
            ("Phillip-a-richmond", "Tooling/other", 1),
            ("DnlRKorn", "Enhancement", 2),
            ("DnlRKorn", "New entry", 10),
            ("bpow", "New entry", 10),
            ("sierra-moxon", "Enhancement", 1),
            ("sierra-moxon", "New entry", 8),
            ("sierra-moxon", "Tooling/other", 1),
            ("tannerzhang", "Enhancement", 2),
            ("tannerzhang", "New entry", 6),
            ("oneilsh", "Enhancement", 3),
            ("oneilsh", "New entry", 2),
            ("sabrinatoro", "Enhancement", 2),
            ("sabrinatoro", "New entry", 1),
            ("flahartyka", "New entry", 1),
            ("gingin77", "Enhancement", 1),
        ],
        columns=["author", "primary contribution", "PRs"],
    )
    contributor_order = [
        "cmungall",
        "kevinschaper",
        "jmcmurry",
        "mellybelly",
        "caufieldjh",
        "nlharris",
        "Phillip-a-richmond",
        "DnlRKorn",
        "bpow",
        "sierra-moxon",
        "tannerzhang",
        "oneilsh",
        "sabrinatoro",
        "flahartyka",
        "gingin77",
    ]
    return contributor_mix, contributor_order


@app.cell(hide_code=True)
def _(alt, contributor_mix, contributor_order, mo):
    contributor_chart = (
        alt.Chart(contributor_mix)
        .mark_bar()
        .encode(
            x=alt.X("PRs:Q", title="Human-authored PRs"),
            y=alt.Y("author:N", sort=contributor_order, title=None),
            color=alt.Color("primary contribution:N", title="Primary contribution"),
            order=alt.Order("primary contribution:N"),
            tooltip=["author", "primary contribution", "PRs"],
        )
        .properties(
            width=760,
            height=390,
            title="Contributors specialized into different lanes",
        )
    )
    mo.vstack(
        [
            contributor_chart,
            mo.md(
                """
                The contributor count understates how differentiated the work became.
                **kevinschaper and jmcmurry ran high-volume new-entry lanes**;
                **cmungall combined existing-entry work with the entire structured
                OpenScientist hypothesis-assessment lane**; **mellybelly and nlharris
                leaned toward enhancements**; and **caufieldjh mixed curation with a
                comparatively large tooling/other lane**. These are work profiles, not
                quality rankings—the PRs differ radically in size and research burden.
                """
            ),
        ]
    )
    return


@app.cell
def _(pd):
    deep_research = pd.DataFrame(
        [
            ("kevinschaper", 70, 69, 2, 0, 0),
            ("jmcmurry", 43, 8, 37, 0, 0),
            ("caufieldjh", 21, 6, 15, 0, 0),
            ("Phillip-a-richmond", 16, 10, 6, 5, 0),
            ("nlharris", 12, 3, 5, 6, 0),
            ("DnlRKorn", 11, 1, 10, 0, 0),
            ("mellybelly", 11, 4, 10, 4, 0),
            ("bpow", 10, 6, 5, 2, 0),
            ("sierra-moxon", 8, 8, 1, 0, 0),
            ("tannerzhang", 8, 6, 3, 0, 0),
            ("cmungall", 6, 1, 3, 1, 3),
            ("oneilsh", 3, 0, 3, 1, 0),
            ("sabrinatoro", 2, 0, 2, 0, 0),
            ("ai4c-agent", 2, 0, 2, 0, 0),
        ],
        columns=[
            "author",
            "any DR",
            "Falcon",
            "Claude/Anthropic",
            "OpenScientist",
            "Asta",
        ],
    )
    provider_totals = pd.DataFrame(
        [
            ("Falcon", 122),
            ("Claude/Anthropic", 104),
            ("OpenScientist", 19),
            ("Asta", 3),
        ],
        columns=["provider", "PRs"],
    )
    return deep_research, provider_totals


@app.cell(hide_code=True)
def _(alt, deep_research, mo, provider_totals):
    providers = (
        alt.Chart(provider_totals)
        .mark_bar()
        .encode(
            x=alt.X("PRs:Q"),
            y=alt.Y("provider:N", sort="-x", title=None),
            tooltip=["provider", "PRs"],
        )
        .properties(
            width=700,
            height=130,
            title="Deep-research provider presence by PR",
        )
    )
    mo.vstack(
        [
            mo.md("## Deep research and OpenScientist"),
            providers,
            mo.ui.table(deep_research, selection=None, page_size=14),
            mo.md(
                """
                Provider counts overlap: 25 PRs included more than one provider. In total,
                223 PRs had a `research/*deep-research*` artifact.

                **OpenScientist had two distinct roles:**

                1. Disease-entry deep research: 19 PRs by nlharris (6),
                   Phillip-a-richmond (5), mellybelly (4), bpow (2), cmungall (1),
                   and oneilsh (1).
                2. Structured hypothesis exploration/assessment under `kb/hypotheses/`:
                   32 PRs, all authored by cmungall. Three added OpenScientist source
                   reports directly (#7433, #7434, #7887); the rest were primarily
                   assessment/reconciliation work.
                """
            ),
        ]
    )
    return


@app.cell
def _(pd):
    size_buckets = pd.DataFrame(
        [
            ("all PRs", "<50", 52),
            ("all PRs", "50–199", 57),
            ("all PRs", "200–499", 50),
            ("all PRs", "500–999", 42),
            ("all PRs", "1,000–4,999", 140),
            ("all PRs", "5,000+", 256),
            ("human-authored", "<50", 21),
            ("human-authored", "50–199", 31),
            ("human-authored", "200–499", 37),
            ("human-authored", "500–999", 36),
            ("human-authored", "1,000–4,999", 100),
            ("human-authored", "5,000+", 197),
        ],
        columns=["cohort", "lines changed", "PRs"],
    )
    order = ["<50", "50–199", "200–499", "500–999", "1,000–4,999", "5,000+"]
    size_quantiles = pd.DataFrame(
        [
            ("all PRs", 597, 406, 3830, 7929, 16206, 206325, 2144613),
            ("human-authored", 422, 728, 4511, 7790, 11089, 15176, 108866),
        ],
        columns=["cohort", "n", "p25", "median", "p75", "p90", "p95", "max"],
    )
    return order, size_buckets, size_quantiles


@app.cell(hide_code=True)
def _(alt, mo, order, size_buckets, size_quantiles):
    size_chart = (
        alt.Chart(size_buckets)
        .mark_bar()
        .encode(
            x=alt.X(
                "lines changed:N", sort=order, title="GitHub additions + deletions"
            ),
            y=alt.Y("PRs:Q"),
            color=alt.Color("cohort:N"),
            column=alt.Column("cohort:N", title=None),
            tooltip=["cohort", "lines changed", "PRs"],
        )
        .properties(width=355, height=210, title="PR diff-size distribution")
    )
    mo.vstack(
        [
            mo.md("## PR length distribution"),
            size_chart,
            mo.ui.table(size_quantiles, selection=None, pagination=False),
            mo.md(
                """
                “Length” means GitHub additions + deletions, including research reports,
                reference caches, and generated artifacts. That makes the distribution
                extremely right-skewed. The all-PR p95 jumps to 206,325 lines because
                scheduled page/dashboard regeneration dominates the upper tail. Excluding
                the three automation accounts gives a more interpretable median of 4,511
                lines and p95 of 15,176, though human PRs still legitimately include large
                research and cache artifacts.
                """
            ),
        ]
    )
    return


@app.cell
def _(pd):
    category_metrics = pd.DataFrame(
        [
            ("New entry", 206, 161, 6955, 2.92, 2.69),
            ("Enhancement", 126, 96, 872, 12.28, 2.45),
            ("Tooling/other", 42, 32, 414, 1.05, 2.21),
            ("OpenSci hypothesis", 29, 29, 618, 0.60, 1.90),
            ("New + enhancement", 10, 9, 9784, 2.67, 3.30),
            ("Review/audit", 9, 8, 122, 0.97, 2.00),
        ],
        columns=[
            "primary contribution",
            "PRs",
            "merged PRs",
            "median lines changed",
            "median merge hours",
            "mean formal AI reviews",
        ],
    )
    return (category_metrics,)


@app.cell(hide_code=True)
def _(alt, category_metrics, mo):
    category_speed_chart = (
        alt.Chart(category_metrics)
        .mark_circle(opacity=0.82)
        .encode(
            x=alt.X(
                "median lines changed:Q",
                scale=alt.Scale(type="log"),
                title="Median changed lines (log scale)",
            ),
            y=alt.Y("median merge hours:Q", title="Median hours to merge"),
            size=alt.Size("PRs:Q", legend=None, scale=alt.Scale(range=[180, 900])),
            color=alt.Color("primary contribution:N", legend=None),
            tooltip=[
                "primary contribution",
                "PRs",
                "merged PRs",
                "median lines changed",
                "median merge hours",
                "mean formal AI reviews",
            ],
        )
    )
    category_speed_labels = (
        alt.Chart(category_metrics)
        .mark_text(align="left", dx=9)
        .encode(
            x=alt.X("median lines changed:Q", scale=alt.Scale(type="log")),
            y="median merge hours:Q",
            text="primary contribution:N",
        )
    )
    category_speed = alt.layer(category_speed_chart, category_speed_labels).properties(
        width=760,
        height=310,
        title="Diff size did not explain merge latency",
    )
    mo.vstack(
        [
            mo.md("## Work shape versus delivery speed"),
            category_speed,
            mo.md(
                """
                The counter-intuitive outlier is **enhancement work**: a median diff of
                only 872 lines, but a 12.28-hour median to merge—more than four times
                the median for new entries nearly eight times larger. The PR discussions
                repeatedly show why: older branches, shared-file edits, inherited base
                failures, and main-branch merges can dominate elapsed time. The
                OpenScientist assessment lane was the opposite: small, tightly scoped,
                and usually merged within an hour.

                This is descriptive, not causal: category, contributor workflow, time of
                day, and branch state are confounded. But it is strong evidence against
                treating changed-line count as a useful proxy for review burden.
                """
            ),
        ]
    )
    return


@app.cell
def _(pd):
    review_bands = pd.DataFrame(
        [
            ("0", 3, None, None),
            ("1", 97, 0.39, 3.80),
            ("2", 145, 2.06, 7.62),
            ("3–4", 143, 4.85, 12.47),
            ("5+", 34, 7.05, 15.19),
        ],
        columns=[
            "formal AI review rounds",
            "human PRs",
            "median merge hours",
            "mean merge hours",
        ],
    )
    review_churn = pd.DataFrame(
        [
            (7746, "nlharris", 8, 8, "Add desmosomopathy to mechanistic nosology enum"),
            (
                7612,
                "mellybelly",
                7,
                31,
                "Add phenotype distribution + EHR profile schema",
            ),
            (7202, "sierra-moxon", 7, 22, "Add SLC35A3-CDG disorder entry"),
            (7438, "cmungall", 6, 7, "Evidence-quality review"),
            (
                7605,
                "kevinschaper",
                6,
                8,
                "Add progressive familial intrahepatic cholestasis",
            ),
            (7686, "sierra-moxon", 6, 10, "Augment Friedreich ataxia"),
            (7585, "caufieldjh", 6, 7, "Add anauxetic dysplasia"),
            (7167, "caufieldjh", 6, 6, "Add CANVAS"),
            (7186, "kevinschaper", 6, 6, "Add/deepen MED13L and MED13"),
            (7629, "kevinschaper", 6, 6, "Add advanced sleep phase syndrome"),
        ],
        columns=["PR", "author", "formal AI reviews", "commits", "title"],
    )
    return review_bands, review_churn


@app.cell(hide_code=True)
def _(alt, mo, review_bands, review_churn):
    review_chart = (
        alt.Chart(review_bands.dropna())
        .mark_line(point=True)
        .encode(
            x=alt.X("formal AI review rounds:N", sort=["1", "2", "3–4", "5+"]),
            y=alt.Y("median merge hours:Q", title="Median hours from open to merge"),
            tooltip=[
                "formal AI review rounds",
                "human PRs",
                "median merge hours",
                "mean merge hours",
            ],
        )
        .properties(
            width=700,
            height=220,
            title="More review rounds correlate with slower merges",
        )
    )
    mo.vstack(
        [
            mo.md("## AI review dynamics"),
            review_chart,
            mo.ui.table(review_bands, selection=None, pagination=False),
            mo.md(
                """
                Of 422 human-authored PRs, 419 had at least one formal AI review. There
                were 1,063 formal AI reviews in total (2.52 per human PR); 34 PRs reached
                five or more rounds. Among the 335 merged human PRs, overall time-to-merge
                was p25 1.04 h, median 2.67 h, p75 15.85 h, and p95 33.07 h.

                High-round cases were not confined to one contributor or one kind of work:
                they included ontology/schema changes, evidence audits, new entries, and
                entry enhancements.
                """
            ),
            mo.md("### Highest formal-review counts"),
            mo.ui.table(review_churn, selection=None, page_size=10),
        ]
    )
    return


@app.cell
def _(pd):
    case_studies = pd.DataFrame(
        [
            (7116, "Scientific correction", 5, 9, 2686, "Endocrine correctness audit"),
            (7202, "Scientific correction", 7, 22, 3840, "SLC35A3-CDG entry"),
            (
                7257,
                "Review-loop friction",
                5,
                8,
                735,
                "Achoo syndrome differential diagnoses",
            ),
            (7491, "Coordination failure", 1, 1, 8611, "Duplicate curation session"),
            (7612, "Review-loop friction", 7, 31, 6744, "Phenotype/EHR profile schema"),
            (7737, "Provenance failure", 3, 3, 7947, "MPI-CDG entry"),
            (7746, "Base-branch churn", 8, 8, 115, "Desmosomopathy enum"),
            (
                7887,
                "Scientific correction",
                2,
                4,
                6846,
                "Amyloid-beta / IBM hypothesis",
            ),
        ],
        columns=["PR", "pattern", "formal AI reviews", "commits", "lines", "case"],
    )
    return (case_studies,)


@app.cell(hide_code=True)
def _(alt, case_studies, mo):
    case_points = (
        alt.Chart(case_studies)
        .mark_circle(size=190, opacity=0.85)
        .encode(
            x=alt.X("commits:Q", title="Commits in PR"),
            y=alt.Y("formal AI reviews:Q", title="Formal AI review rounds"),
            color=alt.Color("pattern:N", title="Observed pattern"),
            tooltip=["PR", "case", "pattern", "formal AI reviews", "commits", "lines"],
        )
    )
    case_labels = (
        alt.Chart(case_studies.query("PR not in [7116, 7257]"))
        .mark_text(dx=9, align="left")
        .encode(
            x="commits:Q",
            y="formal AI reviews:Q",
            text=alt.Text("PR:Q", format="#.0f"),
        )
    )
    case_label_7116 = (
        alt.Chart(case_studies.query("PR == 7116"))
        .mark_text(dx=9, dy=12, align="left")
        .encode(
            x="commits:Q", y="formal AI reviews:Q", text=alt.Text("PR:Q", format="#.0f")
        )
    )
    case_label_7257 = (
        alt.Chart(case_studies.query("PR == 7257"))
        .mark_text(dx=9, dy=-10, align="left")
        .encode(
            x="commits:Q", y="formal AI reviews:Q", text=alt.Text("PR:Q", format="#.0f")
        )
    )
    case_chart = alt.layer(
        case_points, case_labels, case_label_7116, case_label_7257
    ).properties(
        width=700,
        height=300,
        title="Purposeful case sample: review depth versus commit churn",
    )
    mo.vstack(
        [
            mo.md("## Manual deep dive: what the aggregate counts hide"),
            case_chart,
            mo.md(
                """
                I manually read high-churn outliers and PRs surfaced by provenance,
                duplication, and OpenScientist searches. The sample is purposeful—not a
                random sample—and separates four mechanisms that raw “review count”
                collapses together.

                ### Where review materially improved the science

                - [#7116](https://github.com/monarch-initiative/dismech/pull/7116),
                  a manual endocrine audit, shows five rounds paying for themselves. The
                  reviewer caught a **10× prevalence-band error**, bundled PCOS
                  mechanisms, truncated snippets, and evidence-source problems. This is
                  the strongest example of review depth producing substantive value.
                - [#7202](https://github.com/monarch-initiative/dismech/pull/7202),
                  SLC35A3-CDG, mixed seven review rounds with 22 commits. The dialogue
                  corrected LFNG enzymology, rerouted a causal branch, debundled claims,
                  and improved phenotype/conformance modeling. Later cycles also picked
                  up optional polish and unrelated vocabulary migration: scientific
                  value and coordination tax were intertwined.
                - [#7887](https://github.com/monarch-initiative/dismech/pull/7887),
                  the sporadic IBM amyloid-beta hypothesis, is a good OpenScientist
                  calibration case. Review noticed that the prose contradicted its own
                  citation and that two **REFUTE** grades overstated the evidence; both
                  became **PARTIAL**.

                ### Where the process manufactured extra work

                - [#7746](https://github.com/monarch-initiative/dismech/pull/7746)
                  changed only **115 lines** yet received eight reviews. The discussion
                  records repeated main merges and inherited snippet-ratchet failures;
                  effective content barely changed. This is base-state churn, not a hard
                  scientific diff.
                - [#7491](https://github.com/monarch-initiative/dismech/pull/7491)
                  explicitly says two sessions worked the same issue in parallel,
                  duplicating #7489. The duplicate still contained useful treatment
                  content, but the root cause was task-claiming/orchestration failure.
                - [#7612](https://github.com/monarch-initiative/dismech/pull/7612)
                  reached 31 commits, seven formal reviews, and comments labeled as far
                  as **“Round 26.”** Schema design had turned into prolonged co-design in
                  the review channel.
                """
            ),
        ]
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Was there frustration with AI-review back-and-forth?

    **Yes, but the direct evidence is concentrated rather than pervasive.**

    The clearest case is [PR #7257](https://github.com/monarch-initiative/dismech/pull/7257),
    “Add differential diagnoses to Achoo Syndrome.” It had five formal AI reviews,
    eight AI-reviewer comments, eight commits, and merged in 3.35 hours. The author
    explicitly wrote that it was their “last push absent a 🔴 or 🟡,” described
    “five rounds and five approvals,” said the later optional suggestions had
    “decreasing consequence,” and asked that further optional work move to an issue.
    A follow-up also documented reviewer behavioral drift: later rounds incorrectly
    claimed the reviewer could not formally approve, despite earlier rounds doing so.

    That episode exposes two patterns worth fixing:

    - **Approval invalidation:** each author push dismisses the prior approval and
      triggers a full cycle, even when it only addresses an optional nit.
    - **Scope creep across rounds:** later reviews can discover new optional issues
      after the PR is already substantively approved.
    - **Capability drift:** the reviewer can contradict the repository-specific
      workflow and fall back to a generic limitation statement.

    The broader corpus is more mixed. A simple lexical scan found human comments on
    129 PRs using phrases such as “good catch,” “you were right,” or “genuinely useful.”
    Those phrases are not a sentiment model, but they show that repeated review was
    often experienced as valuable correction, not merely friction. The defensible
    conclusion is therefore: **review-loop frustration occurred and is actionable,
    but one should not generalize it to the whole hackathon from this corpus.**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Two provenance failures deserve special attention

    [PR #7737](https://github.com/monarch-initiative/dismech/pull/7737), MPI-CDG,
    exposes a failure that validation could not catch. An AI review suggestion added
    “three-monthly albumin”; a later source audit found that the guideline explicitly
    declined a fixed interval—the three-month number referred to mannose monitoring.
    The author summarized the mechanism precisely: a **deep-research claim laundered
    itself through a review comment**. All 136 validators passed because the false
    specificity lived in free-text description rather than the validated snippet.

    A related discussion in
    [#7605](https://github.com/monarch-initiative/dismech/pull/7605) noted that figures
    originating in Falcon deep research appeared more trustworthy when the reviewer
    independently repeated them. Together, these cases show that an AI reviewer is not
    an independent source merely because it phrases the same unsupported assertion a
    second time. Provenance controls need to cover free text and reviewer-suggested
    claims, not only structured evidence snippets.

    ## Recommendations for the next sprint

    1. **Adopt a stopping rule.** Once a PR is approved, only critical/important
       findings should reopen it; optional improvements become follow-up issues.
    2. **Review the delta.** Small pushes should receive delta-focused checks rather
       than a fresh full audit. A main-only merge with an unchanged effective diff
       should not invalidate approval.
    3. **Separate base health from PR health.** Report inherited CI failures and
       branch-conflict work as coordination state, not new defects in the contribution.
    4. **Claim curation tasks.** A lightweight issue lease would prevent parallel
       agents from independently curating the same disorder.
    5. **Extend provenance to prose.** Require source-linked support for precise
       monitoring intervals, prevalence figures, and similar free-text claims—even
       when the claim originates in an AI review suggestion.
    6. **Measure why rounds happen.** Tag each additional round as scientific defect,
       schema/design negotiation, base churn, or optional polish. The current review
       count mixes high-value correction with avoidable process churn.

    The main conclusion is not “less AI review.” It is **preserve adversarial
    scientific review while removing automatic re-audit, base-branch noise, and
    provenance laundering**. The cases above show that both halves matter.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Methods and limitations

    - PR discovery used GitHub search with `created:>=2026-07-29`; metadata,
      comments, and reviews came from GitHub's API. File lists were separately
      paginated through the REST API so all 94,603 changed-file records were
      considered and `added` could be distinguished from `modified`.
    - No PR had more than 100 comments or 100 formal reviews, so the collected
      discussion bodies were complete at the API limits used.
    - `github-actions`, `dependabot`, and `ai4c-agent` are treated as automation for
      human-contributor counts. The automation PRs remain in whole-cohort totals.
    - Contribution type is path/title based. “New entry” requires an `added`
      `kb/disorders/*.yaml`; “enhancement” requires `modified`. This is reliable for
      the headline distinction, but the smaller review/tooling/other classes involve
      judgment.
    - Deep research requires a changed `research/*deep-research*` artifact. Work that
      used research transiently without committing an artifact will be missed.
    - Frustration is assessed conservatively from explicit contributor language and
      objective churn. Absence of such language is not evidence of satisfaction.
    - The qualitative deep dive is a purposeful case sample: high-review and
      high-commit outliers plus PRs surfaced by provenance, duplication, and
      OpenScientist searches. It is designed to identify mechanisms, not estimate
      their prevalence.
    - This is a snapshot of a fast-moving repository. Open/merge outcomes will change
      after 2026-08-03 22:53 UTC; PR-author counts do not include co-authors.
    """)
    return


if __name__ == "__main__":
    app.run()
