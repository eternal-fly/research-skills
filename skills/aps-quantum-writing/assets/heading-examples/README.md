# APS heading typography examples

These are synthetic layout examples, not research papers, scientific results, official APS templates, or publisher-identical facsimiles. Heading presence and wording are author choices. Do not insert Introduction, Conclusions, or Outlook automatically.

## Rebuild

Prerequisites: an existing working pdfLaTeX distribution, official REVTeX 4.2f, and the standard etoolbox package. No installer or network access is invoked by the build script.

From this directory, run:

```sh
bash build-preview.sh
```

Five individual PDFs appear in `build/`. Each source is compiled twice. Alternatively, run `pdflatex prl-chosen-headings.tex` twice. Keep both helper files next to the sources. All input paths are relative; no original workspace path is required.

The combined five-page PDF is supplied separately. It is a straightforward concatenation in this order:

1. `prl-chosen-headings.tex`: optional PRL headings, main/secondary/deeper levels, Conclusions, Note added, acknowledgments, and data availability.
2. `prl-unheaded-opening.tex`: no Introduction title; author-selected descriptive heading and Outlook.
3. `prl-no-main-headings.tex`: neither opening nor closing main-text headings.
4. `regular-production-preview.tex`: numbered standalone hierarchy, opt-in bold italic third level, unnumbered acknowledgments and data availability.
5. `nonprl-letter.tex`: optional italic-period run-in headings, including current PRA/PRResearch Letter data availability and appendix practice.

## Helper contract

- `\prlrunin{Heading}`: PRL main-text italic heading plus italic em dash, no period before the dash.
- `\apsletterrunin{Heading}`: selected non-PRL Letter italic heading plus period and ordinary word space.
- `\apssecondaryrunin{Heading}`: roman heading, colon, and em space.
- `\apsdeepprlrunin{Heading}`: PRL deeper italic heading, period, and ordinary word space.
- `\prlrunin{Note added.}` intentionally preserves the separate PRL Note added.— exception. Do not run a global period-before-dash deletion.
- Heading text is not uppercased or normalized. Supply words without terminal punctuation, except the Note added case above. The helpers do not create section counters, ToC entries, or bookmarks. They are not drop-in semantic replacements for numbered section commands.
- These commands use ordinary paragraphs, not boxes, tables, or forced line breaks. Body text returns to upright on the same line where space permits and wraps naturally thereafter. Paragraph indent comes from the active template.
- Load and call the applicable helper only after selecting journal and article type. Do not globally redefine `\section`.

PRL's native acknowledgments environment prints no heading in REVTeX 4.2f, so the PRL samples safely add one explicit run-in title inside it. The non-PRL Letter sample instead uses its explicit run-in title directly: also opening the native acknowledgments environment would produce an extra standalone title.

## Regular third-level font preview

Loading `regular-preview-hooks.tex` alone changes nothing. Explicitly call `\EnableAPSRegularThirdLevelPreview` only for an APS Regular Article in reprint mode. It adds bold to the dedicated numbered/starred third-level font hooks while retaining native numbering, alignment, and other section commands.

The opt-in checks that the active class is REVTeX with APS/reprint, rejects PRL, checks the current dispatchers for the relevant hook mechanism, and refuses to replace preexisting hooks. An incompatible or modified future template emits a warning and stays unmodified. Inspect the PDF and logs rather than assuming the preview was enabled. The native 4.2f third level is italic but not bold; the February 2026 APS guide describes bold italic.

## Letter data-availability and appendix caveat

The February 2026 APS guide's general data-availability clause says a principal heading for journals other than PRL. The current Letter examples show a different production convention. This PRA Letter preview deliberately uses the run-in italic-period form observed in:

- [PRA 113, L030201 (2026)](https://doi.org/10.1103/qw5d-5ztg), p. 3
- [Physical Review Research 8, L032025 (2026)](https://doi.org/10.1103/2pg6-vd1j), p. 5
- [Physical Review Research 8, L032046 (2026)](https://doi.org/10.1103/g2z2-2w2h), p. 5

The first two also support run-in Letter appendix headings. This is an evidence-based production-preview choice, not a claim that the guide states an explicit Letter exception. For another journal/article type or a mandatory current template, recheck that specific target. Never transplant PRL End Matter rules to these Letters.

## Sources and verification

- [APS REVTeX page and official 4.2f download](https://journals.aps.org/revtex)
- [APS Journals Style Guide, February 2026](https://res.cloudinary.com/apsphysics/image/upload/APS_Journals_Style_Guide_Authors022326_guzwhx.pdf), printed pp. 12–15, 19, 23

Historically verified with pdfTeX 1.40.26, LaTeX2e 2024-11-01 patch level 2, and official REVTeX4.2f. These were inherited results at the English v1.0.0 release, not a new compilation in its packaging environment.

On 2026-10-20, the five exact v1.0.0 public examples were independently recompiled twice with pdfTeX 1.40.24, LaTeX2e 2021-11-15 patch level 1, and official REVTeX 4.2f. All five fresh PDFs passed visual inspection and 120 new PDF/log checks; a clean script replay passed too. No source changes were needed. See the [revalidation report](../../docs/HEADING-REVALIDATION-2026-10-20.md) for logs, evidence, reproduction instructions, and the explicit list of historical tests not rerun.

Fonts in these previews are Computer Modern; publisher font families, final page geometry, and exact publication pagination are not reproduced. These are microtypography previews, not final length certification.
