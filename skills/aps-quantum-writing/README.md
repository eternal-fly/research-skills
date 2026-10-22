# APS Quantum Writing

**One scientific question. A coherent paper. Figures that explain the science.**

APS Quantum Writing is an English-language agent skill for planning, writing, and illustrating quantum and related physics research. It keeps the scientific argument, evidence, prose, and final layout connected throughout a manuscript workflow.

**Author:** Luofei Wang · **Version:** 1.2.0 · **License:** custom noncommercial source-available terms; see [LICENSE](LICENSE).

> This project is source-available, not OSI-approved open-source software. Noncommercial use and private modifications are permitted. Commercial use and public redistribution/repackaging require separate permission, subject to the license's platform and third-party exceptions. Ordinary research outputs are treated separately.

Release record: [1.2.0 validation](docs/RELEASE-1.2.0.md). The supplied figure revision remains documented in [English](docs/FIGURE-REVISION-2026-10-22.md) and [Chinese](docs/FIGURE-REVISION.zh-CN.md).

## Start here

1. Download `aps-quantum-writing-1.2.0.zip` and its checksum from the [v1.2.0 release](https://github.com/eternal-fly/research-skills/releases/tag/v1.2.0).
2. Keep the complete `aps-quantum-writing` folder together. Read [installation](docs/INSTALL.md) for project-local, personal, and manual use.
3. Ask your agent to read [SKILL.md](SKILL.md), then provide the manuscript, derivations/data, intended journal, and article type.

```text
Use aps-quantum-writing to develop this manuscript for PRL.
Start from the existing scientific results. Identify the central question,
plan the argument and figures, and continue through drafting and final review.
Choose headings according to the argument; do not force Introduction or Conclusion labels.
Use only verified references and supplied or reproducibly computed data.
```

The skill supplies instructions and reusable assets. Your agent runtime supplies the model, document access, plotting tools, and LaTeX environment. It does not run unattended merely because the folder is installed.

## Three branches

| Branch | Purpose | Entry |
|---|---|---|
| **PLANNING** | Background, journal/type, central question, outline, title, figure plan, and final scientific assessment | [Planning](references/branch-planning.md) |
| **WRITING** | Clear physics, motivated proofs, defined notation, natural prose, and accurate claims | [Writing](references/branch-writing.md) |
| **FIGURES** | Data plots, dense readable scientific schematics, layout, export, and visual review | [Figures](references/branch-figures.md) |

Journal and formatting references are supporting routes, not additional top-level branches.

## Journal coverage

PRL, PRA, PRB, PRX Quantum, Physical Review Applied, Physical Review X, and Physical Review Research. Article type matters: a Letter and a Regular Article in the same journal can use different heading typography. The skill records current official requirements separately from observed publication practice and configurable design preferences.

## What it emphasizes

- A central scientific question that a reader can state in one sentence.
- Conceptual unity: necessary technical links or genuinely complementary evidence, rather than a list of loosely related results.
- Motivation-first exposition of proofs, with technical dependencies checked separately.
- Direct, readable academic prose using standard terms and defined symbols.
- Positive statements of applicable conditions, without unnecessary author-defensive lists of unperformed work.
- Scientifically informative diagrams with recognizable internal structure, meaningful interfaces, and clear training/update/frozen-state distinctions when relevant.
- Compact data panels with properly aligned y-axis content, centered bottom labels, readable final-size typography, and near-square scalar axes when the science permits.
- Journal/type/role-aware heading checks, including PRL run-in dashes, other Letters' periods, independent numbered headings, and special end-matter roles.

## Figure planning and full-manuscript narrative

Version 1.2.0 integrates the supplied fixed [figure planning record](references/figure-planning-record.md), conditional [quantum-domain recipes](references/quantum-figure-recipes.md), and single-column-first decision process. Main-text guidance connects the central question, obstacle, key idea, proof or evidence, and physical answer. Appendices and Supplemental Material follow the same direct scientific style while retaining necessary assumptions, uncertainty and negative results.

The [release validation](docs/RELEASE-1.2.0.md) separates newly executed manuscript/figure checks from the supplied literature-review records and historical heading validation. The narrative cases are complete synthetic short manuscripts with Supplements, not real research or a statistical efficacy benchmark.

## Examples

- [Abstract narrative guide](references/abstract-narrative.md): contribution, core method, reasoning, and journal/article-type choices; [evidence and scope](references/abstract-evidence.md).
- [1.2.0 validation](docs/RELEASE-1.2.0.md): full-manuscript and Supplement behavior checks, figure smoke test, and execution boundaries.
- [1.1.0 validation](docs/RELEASE-1.1.0.md): preserved earlier abstract and heading evidence.
- [Five-page heading PDF](assets/heading-examples/APS-heading-layout-examples.pdf): optional PRL headings, unheaded openings, no main-text headings, Regular hierarchy, and non-PRL Letter typography.
- [Editable heading sources](assets/heading-examples/README.md).
- [Synthetic data-plot captions](assets/figure-examples/CAPTIONS.md) and [mechanism example captions](assets/mechanism-examples/captions.md).

Examples are synthetic demonstrations, not research results. Some legacy figures are retained as technical examples; they are not a claim that every design preference has already been applied to every image.

## Documentation

- [Installation and updates](docs/INSTALL.md)
- [Detailed usage and prompts](docs/USAGE.md)
- [Evidence and provenance](docs/PROVENANCE.md)
- [Validation and reproducibility](docs/VALIDATION.md)
- [Contribution policy](CONTRIBUTING.md)
- [Security and sensitive manuscripts](SECURITY.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)
- [Changelog](CHANGELOG.md)

## Optional plotting tools

The writing instructions have no Python dependency. To regenerate the bundled scientific examples, use an isolated Python environment and the optional dependencies in [requirements.txt](requirements.txt):

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
python scripts/generate_figure_examples.py --out /path/to/new-output/figures
python scripts/generate_mechanism_examples.py --out /path/to/new-output/mechanisms
```

Choose a new output directory to preserve the shipped examples. Heading examples require a working LaTeX installation and REVTeX; instructions are included with the sources. Minimum compatible dependency versions are not claimed beyond the environment actually tested.

## Research integrity

The provenance index contains 700 unique DOIs, 100 per journal. That is not a claim of 700 complete new reviews or 700 full visual audits; review depth and source versions are documented explicitly. The skill does not certify mathematical correctness, novelty, journal acceptance, or publication-ready figures without manuscript-specific verification.

This is an independent project. APS, OpenAI, and the cited projects have not endorsed it.
