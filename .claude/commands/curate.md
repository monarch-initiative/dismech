---
description: Curate a given disorder, either de-novo, or augment an existing one. A list of deep research providers may be specified.
argument-hint: [DISORDER_NAME] ( using [DEEP_RESEARCH_PROVIDER] )
---

## Prerequisites Check

Before starting curation, verify your environment has the required tools. If any are missing, proactively ask your human manager for help instead of attempting workarounds.

### 1. `just` Command Runner

Test if available:
```bash
just --version
```

**If missing, ask your human:**
> "I need the `just` command runner to proceed with curation workflows. This tool is essential for running validation and research commands. Would you like me to guide you through installing it? See https://github.com/casey/just#installation"

**Do NOT** attempt to work around missing `just` by running commands manually. The `just` commands handle complex pipelines that shouldn't be replicated ad-hoc.

### 2. Deep Research Provider API Key

This workflow uses deep research APIs to gather scientific literature from authoritative sources.

**Recommended: Edison Scientific (falcon)**
- Most comprehensive for biomedical literature
- Provides access to PubMed, clinical databases, and full-text articles

**If not configured, ask your human:**
> "I need a deep research provider API key to gather literature for this disorder. I recommend Edison Scientific (falcon) for the most comprehensive biomedical coverage.
>
> To get started:
> 1. Visit https://platform.edisonscientific.com/
> 2. Create an account (if needed)
> 3. Navigate to: Account → Profile → + Create new token
> 4. Copy the API key and set it in your environment:
>    ```bash
>    export EDISON_API_KEY=your_key_here
>    ```
>
> Alternative providers (perplexity, openai, cyberian) are also available but may have less specialized biomedical coverage. Would you like to proceed with Edison/falcon?"

**Other provider options:**
- `perplexity` - General web search with scientific literature
- `openai` - GPT-based research (requires OpenAI API key)
- `cyberian` - Alternative research provider

### 3. Python Environment

Verify `uv` is available:
```bash
uv --version
```

If missing, ask your human:
> "I need the `uv` Python package manager. Would you like me to guide you through installing it? See https://github.com/astral-sh/uv#installation"

## Curation Workflow

Once prerequisites are confirmed, curate the disorder specified in $ARGUMENTS.

**IMPORTANT:** You MUST consult the `initiate-new-disorder-creation` skill for detailed instructions on the curation process.

**Deep Research Provider Selection:**
- If the user specifies a deep research provider(s), use at least those provider(s)
- If not specified, **default to falcon (Edison Scientific)** for optimal biomedical literature coverage
- Multiple providers can be used sequentially for cross-validation

**Example commands:**
```bash
just research-disorder falcon "Parkinson Disease"
just research-disorder perplexity "Parkinson Disease"
```

## Managing Up: Communication Guidelines

When you encounter issues or need human input:

1. **Be specific about what you need** - Don't just say "there's an error", explain what's missing and why it's needed
2. **Provide actionable next steps** - Give clear instructions or links
3. **Explain the impact** - Help your human understand why this dependency matters
4. **Offer to help** - Ask if they'd like guidance installing or configuring tools
5. **Don't attempt workarounds** - If a core tool like `just` is missing, stop and ask rather than trying to reverse-engineer the workflow

**Good example:**
> "I need the Edison API key to access biomedical literature databases. This will allow me to gather high-quality evidence from PubMed and clinical sources for the disorder you want to curate. Here's how to get one: [steps]. Should I wait while you set this up, or would you like to use an alternative provider?"

**Bad example:**
> "API key not found. Trying alternative approach..." ← Don't do this
