# Third-party notices

APS Quantum Writing, public English edition. Source and component audit date: October 9, 2026. See [provenance](docs/PROVENANCE.md) for evidence scope and the distinction between inherited verification and current-release checks.

## Original project material

Author: **Luofei Wang**.

The author-approved [project LICENSE](LICENSE) is a custom noncommercial source-available license. It is not an OSI open-source license. The separate third-party licenses below apply only to their identified components; they do not license the entire skill, its original observations, scripts, or illustrations. Conversely, a restriction on original project material does not add a restriction to a third party's separately licensed material.

This notice does not claim that this edition has been published or endorsed by APS or another cited organization.

## Research Writing Assistant

The source work selectively consulted [Norman-bury/research-writing-skill at commit 6f7959554b4614d879d79cb4ece9ed04a7c8a88c](https://github.com/Norman-bury/research-writing-skill/tree/6f7959554b4614d879d79cb4ece9ed04a7c8a88c). The recorded influence concerns natural prose, evidence-to-claim relationships, connected workflows, and scientific-figure design. Explanations, examples, and APS-specific integration were rewritten for this project. The upstream project did not validate this skill's APS-specific capabilities.

The upstream material is MIT-licensed. Its copyright holder is Xunchang (romanized here); the authoritative, exact 2026 copyright line and the complete license remain unchanged in [RESEARCH-WRITING-SKILL-MIT.txt](licenses/RESEARCH-WRITING-SKILL-MIT.txt). Do not replace that line with this project's author. The [fixed-commit upstream license](https://raw.githubusercontent.com/Norman-bury/research-writing-skill/6f7959554b4614d879d79cb4ece9ed04a7c8a88c/LICENSE) is the original reference.

Retaining the MIT notice neither makes this whole project MIT-licensed nor implies that every upstream file is bundled.

## DejaVu fonts embedded in synthetic examples

The identified PDFs in `assets/figure-examples/` and `assets/mechanism-examples/`, and the applicable figure material in `assets/layout-example/layout.pdf`, embed subsets of DejaVu Sans, DejaVu Sans Bold, and DejaVu Sans Oblique. The historical audit also checked font names in five EPS exports. Those redundant EPS exports are excluded from this lightweight public edition; the plotting scripts can regenerate them. The source audit recorded DejaVu Version 2.35, matching the name, version, and copyright records of fonts bundled with the generating Matplotlib 3.10.8 distribution.

The embedded records identify Bitstream, Inc. (2003), Tavmjong Bah (2006), and the public-domain status of DejaVu changes. The complete unchanged notice is [DEJAVU-LICENSE.txt](licenses/DEJAVU-LICENSE.txt), copied from Matplotlib's `mpl-data/fonts/ttf/LICENSE_DEJAVU`. See the [official DejaVu license page](https://dejavu-fonts.github.io/License.html).

These notices concern the identified fonts, not the scientific text, data, plotting code, or original graphic compositions. No complete standalone TTF installation files are bundled.

## AMS Computer Modern fonts embedded in layout examples

The source audit of `assets/layout-example/layout.pdf` identified Computer Modern Type 1 subsets CMBX12, CMR10, CMTI9, CMR9, CMTI10, CMMI10, CMEX10, CMSY10, CMMI7, and CMR7. The five-page `assets/heading-examples/APS-heading-layout-examples.pdf` identified CMBX12, CMR10, CMTI10, CMBX9, and CMBXTI10.

The embedded cleartext headers identify version 003.002, Copyright (c) 1997, 2009 American Mathematical Society, and SIL Open Font License 1.1. All listed font names occur in the original AMSFonts Reserved Font Name list. Original embedded declarations are retained.

The complete unchanged license and Reserved Font Names are in [AMSFONTS-OFL-1.1.txt](licenses/AMSFONTS-OFL-1.1.txt), sourced from [CTAN's original AMSFonts file](https://tug.ctan.org/fonts/amsfonts/doc/OFL.txt). The [AMSFonts project information](https://ctan.org/tex-archive/fonts/amsfonts?lang=en) distinguishes the fonts from LaTeX support files. The OFL here applies to the identified fonts, not to REVTeX or the whole project. Its terms do not require a document made with the fonts to use the OFL.

The [embedded-font record](evidence/embedded-fonts.json) preserves the inherited per-PDF hashes and 53 font-resource records across 10 source asset PDFs. It identifies the audited source assets; regenerated or replaced assets require a separate check. Font subsets are not claimed to be byte-identical to the complete original fonts. Extracted standalone font files are not distributed.

## Paper metadata and evidence

The evidence index has 700 DOI records from seven journals. The legacy source archive held 390 original observation snippets and 10 late-reserved PRL placeholders, with 128 truncated snippets; the later expansion added 300 main-body/main-caption review records. This English edition preserves metadata and translated original rule-level observations and locators, not the complete historical per-paper notes. Review, image-inspection, sampling, and non-blind-validation limitations are described in [provenance](docs/PROVENANCE.md).

Titles, DOI identifiers, source-version facts, and public links identify the literature. Paper text, source figures, and their rights remain with their respective rightsholders. This edition does not bundle downloaded paper PDFs, full abstracts, JATS bodies, original paper artwork, or paper-page screenshots. Public access through APS, a repository, or arXiv does not automatically grant permission to redistribute those materials. Any future inclusion requires a version-specific rights and attribution review.

## Dependencies and other references

Plotting scripts use NumPy, SciPy, Matplotlib, and their dependencies. Layout examples use LaTeX and REVTeX. Complete dependency packages, REVTeX class files, and complete font installations are not copied into this skill. Their own distributions and licenses remain authoritative when installing or using them.

Official guides and other publicly referenced design material inform the documentation without transferring their licenses to the whole project. APS, the American Mathematical Society, upstream contributors, and font authors are not represented as sponsors, certifiers, or endorsers.

These notices record identified components and source evidence. They are not a legal certification that every possible third-party right has been exhaustively reviewed. Update the component record when adding or replacing fonts, images, templates, code, or quoted literature.
