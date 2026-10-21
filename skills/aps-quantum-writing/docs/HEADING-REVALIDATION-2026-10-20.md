# Independent v1.0.0 heading revalidation

## Result and provenance

On 2026-10-20 (America/Denver), the five public heading examples from tag
`v1.0.0`, commit `b3bde106545d33608e5948929b3330fcd68a4e84`, were independently
compiled and visually inspected. All five passed. No TeX source or helper
correction was necessary. This document closes the fresh-compilation evidence
gap for these five examples; it does not retrospectively change the release-time
validation environment.

The original release source and helper text was used without edits. The Windows
checkout converted the tag's LF line endings to CRLF; this was the only byte
difference in the compiled inputs. The
existing combined preview PDF was not used as evidence of fresh compilation and
was not replaced. The original 1.0.0 checksum manifest is preserved as
[v1.0.0-SHA256SUMS](../evidence/v1.0.0-SHA256SUMS); the skill-root manifest now
describes the 1.1.0 files.

## Environment and procedure

- Windows; pdfTeX 3.141592653-2.6-1.40.24, TeX Live 2022.
- LaTeX2e 2021-11-15 patch level 1.
- Official REVTeX `2022/06/05 4.2f`, obtained from the
  [CTAN distribution](https://mirrors.ctan.org/macros/latex/contrib/revtex.zip).
- The preinstalled 4.2e was not used. The downloaded source was unpacked with
  `tex -interaction=nonstopmode revtex4-2.dtx`; a process-local `TEXINPUTS`
  selected the resulting 4.2f class and APS support files. No global TeX files
  were modified. The `.fls` records identify the files actually loaded.
- Each source was compiled twice using `-no-shell-escape`,
  `-interaction=nonstopmode`, `-halt-on-error`, and `-recorder`.
- Poppler rendered every new PDF at 1600 pixels on its long edge. All five full
  pages were inspected for heading appearance, wrapping, spacing, clipping,
  duplicate headings, and unintended inserted headings.
- `pdfplumber 0.11.9` supplied glyph fonts and coordinates. Poppler text
  extraction independently checked punctuation. The accompanying script
  executed 120 checks, all passing. These are newly defined checks of the five
  examples, not the inherited 32 assertions.
- The final parameterized PowerShell build script was then replayed in a second
  empty directory: another 10 successful compiler invocations and the same
  120/120 checks. This is a reproducibility replay, not ten additional examples
  or 240 distinct checks. In total, 20 compiler invocations were completed.

## Per-example findings

| Source | Two-pass result | Visual and glyph-level findings |
|---|---|---|
| `prl-chosen-headings.tex` | Pass; one page | Main labels and em dashes are CMTI10; upright CMR10 body resumes on the same baseline. No period before the main-heading dash; `Note added.—` is retained. Secondary label is roman with colon; deeper label is italic with period. Only one acknowledgments label. |
| `prl-unheaded-opening.tex` | Pass; one page | Opening remains unheaded. Descriptive heading, Outlook, acknowledgments, and data availability have the intended PRL run-in typography. |
| `prl-no-main-headings.tex` | Pass; one page | No opening or closing main-text heading inserted. Only acknowledgments and data availability have run-in labels. |
| `regular-production-preview.tex` | Pass; one page | Native I./A./1. hierarchy remains standalone and centered. First two levels are CMBX9; third level is CMBXTI10 (bold italic). Unnumbered acknowledgments/data headings remain standalone. Log confirms the opt-in font hooks were enabled. |
| `nonprl-letter.tex` | Pass; one page | All six Letter labels use italic CMTI10, period and visible word space, then upright body on the same baseline. No em dash. Secondary label is roman/colon. No duplicate acknowledgments heading. |

The Regular third-level paragraph crosses the balanced column boundary after
its first two lines. This is normal two-column balancing, not a detached heading
or clipping defect. All page content remained legible and inside page bounds.

## Log findings

All ten first-run invocations and all ten replay invocations returned zero.
Every first pass emitted the expected `Label(s) may have changed` rerun warning;
it disappeared on every second pass. Second-pass logs contain no LaTeX/package
warnings, overfull/underfull boxes, missing-character messages, or TeX errors.
All logs confirm REVTeX 4.2f. The Regular preview reports
`Regular third-level bold font hooks enabled`.

The `No file <example>.bbl` informational lines remain: these synthetic examples
have no citations or bibliography content and are built with two pdfLaTeX
passes, as documented. They are recorded here rather than described as absent.

## Reproduce and inspect evidence

The [machine-readable record](../evidence/heading-revalidation-2026-10-20.json)
identifies the source commit, environment, counts, and unexecuted historical
suites. The [evidence bundle](../evidence/heading-revalidation-2026-10-20.zip)
contains exact input TeX files, original and replay logs/stdout/recorder files,
five fresh PDFs and page PNGs, extracted text, the check results, the build and
audit scripts. Its file manifest records SHA-256 hashes. The public export
prepared on 2026-10-21 replaces local path prefixes in text logs with named
placeholders; unmodified originals remain in the local audit workspace. PDFs,
PNGs, exact input TeX, and automated check results are unchanged. The official
upstream archive is obtained separately using its recorded URL and SHA-256.
The scripts accept new paths.

To reproduce with a working pdfLaTeX and PowerShell installation:

1. Check out the exact commit above in a fresh clone.
2. Download the official `revtex.zip`, verify its hash against the machine-readable
   record, and extract it; in its `revtex` directory run
   `tex -interaction=nonstopmode revtex4-2.dtx`.
3. Run the bundled script with a new output directory:

   ```powershell
   ./run.ps1 -Repository /path/to/research-skills -RevtexDirectory /path/to/revtex -OutputDirectory /path/to/new-build
   ```

4. With Python `pdfplumber==0.11.9` and Poppler `pdftotext` on PATH, run
   `python audit.py /path/to/new-build`. It writes `pdf-checks.json` and returns
   nonzero on a failed check. The font checks intentionally describe this
   Computer Modern environment; other fonts require a separate review.
5. Render all five PDFs with `pdftoppm -scale-to 1600 -png -singlefile` and
   inspect the full pages. Automated checks do not replace visual inspection.

## Explicit limits and inherited results

The historical 29-source compilation matrix, 32 assertions, four invalid-option
controls, other journal-option variants, and starred-third-level guard cases
were **not rerun**. Their historical records remain inherited. Only the five
public examples and their documented active paths were freshly exercised.

The release-time metadata reports seven distribution tests and two numerical
tests; these are inherited metadata, not reconstructed execution counts. The
checked-in v1.0.0 suite actually contains five distribution methods and two
mechanism methods (one file-presence check and one numerical-model test), seven
methods total. The full suite, figure generation, behavior review, and
literature/publisher-rule review were **not rerun as part of this heading audit**.
A separate, current five-test distribution check of
the modified documentation was executed with
`python -m unittest discover -s tests -p test_release_layout.py -v`: **5/5
passed**. This checks documents, local links, English instructions, DOI metadata,
and the three branch entries. It is separate from the historical seven-test
suite; the numerical tests were not executed.

This result establishes compatibility in the recorded environment, not all
LaTeX versions, all journal/article combinations, publisher-identical layout,
publication-length compliance, or present-day editorial policy. The Letter
data-availability/appendix convention remains the explicitly qualified preview
choice documented in the original heading README.
