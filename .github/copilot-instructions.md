# CLAUDE.md for 

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

WARNING: read this closely as it gets a bit meta.

This is a repo for a copier project intended to allow people to set up their github repo with AI github actions.

- template files are in `template/`
- all other files are for this repo itself

So for example

- template/.github/workflows/claude.yml - A template that is copied into a users target repo to set up claude gh actions
- .github/workflows/claude.yml - The actual github actions for this repo itself.

This repo eats its own dogfood! We will occasionally run

`copier copy template .`



