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
    - There is **one clear, explicit frustration episode** in the corpus: PR #7257.
      It describes five rounds/five approvals, diminishing returns from successive
      optional suggestions, and reviewer capability drift. That is real evidence of
      review-loop frustration, but not evidence that frustration was widespread.
    """)
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
            height=260, title="Primary contribution type (exclusive classification)"
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
        .properties(height=130, title="Deep-research provider presence by PR")
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
        .properties(width=270, height=210, title="PR diff-size distribution")
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
        .properties(height=220, title="More review rounds correlate with slower merges")
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
    - This is a snapshot of a fast-moving repository. Open/merge outcomes will change
      after 2026-08-03 22:53 UTC; PR-author counts do not include co-authors.
    """)
    return


if __name__ == "__main__":
    app.run()
