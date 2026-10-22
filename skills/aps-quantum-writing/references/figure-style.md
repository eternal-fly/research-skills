# APS figure generation: technical style baseline

Applies to PRL, PRA, PRB, PRX Quantum, Physical Review Applied, Physical Review X, and Physical Review Research. Styling for the original four journals was checked on 2026-10-07; official requirements for the three added journals were rechecked on 2026-10-09. Load this reference only when generating or modifying figures/tables. Deliverables should prioritize appearance at final size: artwork, reproducible Python scripts, and necessary captions. Preserve real data and the paper's own visual semantics instead of imposing example layouts on every article.

## Distinguish three kinds of authority first

1. **Published APS requirements/guidance:** the original four journals share Style Basics and the Style Guide. Specific guidance includes a single-column width of approximately 85 mm; minimum capital-letter/numeral height of 2 mm at final size; data-point diameter of at least 1 mm; curve width of at least 0.18 mm, approximately 0.5 pt; and upright panel labels (a), (b). Keep quantities and units distinct, with units in parentheses. These are instructions on official pages, not evidence that each journal has its own visual template. [Style Basics](https://journals.aps.org/authors/style-basics)
2. **Observations from published figures:** the review sampled five version-of-record (VOR) PDFs per journal, 20 in total. Figure organization, typography, and colors vary even within a journal. This is not an image census of all 400 papers; the 400-paper writing evidence remains unchanged. See the [public provenance record](../docs/PROVENANCE.md).
3. **Package defaults:** the fonts, colors, line-width margins, tick directions, and canvas heights below are adjustable practical choices, not mandatory APS standards. Do not claim that PRL requires blue/red or PRB requires a particular font.

## Planning and column preference

Use the [fixed planning record](figure-planning-record.md) to connect the physical discrimination, panel roles, data lineage and visual choices. Unless specified otherwise by the user, start at single-column width. Move to double column only when an essential mechanism/comparison, scientific geometry, or final-size legibility cannot be retained after reasonable layout repair; record that decision and recheck the actual export/insertion size. This is a configurable workflow preference, not an APS requirement. Multiple panels can fit one column, and even two coupled panels can need both columns. Near-square scalar plotting areas and the exceptions below remain in force.

## Shared baseline: inspect the generated appearance

| Item | Package default or check |
|---|---|
| Final canvas | Single-column: 85 mm. The 178 mm double-column example is only a working preset; use the target REVTeX/template's actual textwidth. Set the width before plotting. |
| Fonts | DejaVu Sans text with matching MathText; axis labels, ticks, and legends at 9 pt. Example axis labels with subscripts use 12 pt to keep subscripts large enough. No local LaTeX dependency. |
| Glyph height | Check actual glyph height: 2 mm cannot simply be converted to a 5.67 pt font size. Recheck after changing fonts, subscripts, or scale. In the examples, a 9 pt capital H is approximately 2.31 mm high; a 70%-size subscript H under a 12 pt setting is approximately 2.16 mm. |
| Curves/frames | Data curves: 1.1 pt; axes frames: 0.7 pt; error bars: 0.8 pt; caps: 0.7 pt. Do not conceal discrete structure by thickening lines. |
| Markers and line styles | Circle/square markers at 4 pt; circle diameter approximately 1.41 mm. scatter's s is an area, so 4 is not a diameter; circles can start at s = 16 pt², followed by a check of the actual marker. |
| Categorical colors | Blue #0072B2, vermilion #D55E00, green #009E73, purple #CC79A7, dark gray #222222. Also distinguish categories by shape, line style, or text, not color alone. |
| Heatmaps | cividis can suit a one-directional nonnegative quantity. RdBu_r centered at zero can suit signed differences with a meaningful zero. Add sign labels and dashed/solid contours to distinguish positive and negative contours in grayscale. Colormaps are choices; data semantics come first. |
| Axes | White background, no grid by default, inward ticks, complete thin frames; all are adjustable. Use a small number of major ticks and avoid false precision. Choose logarithmic axes for a scientific reason without concealing zero/negative values. |
| Legends | 9 pt, frameless, in reserved whitespace or controlled positions outside the axes. Keep category colors/markers consistent across panels. A few curves can be labeled directly. |
| Panels | Upright (a), (b), etc.; examples use bold 9 pt labels at upper left. Move them as content requires. Keep them clear of data and maintain contrast on heatmaps. |
| Mathematics/units | Italic single-letter variables; upright units, text, and multi-letter functions. Time Jt and Energy E/J indicate dimensionless normalization; actual units take forms such as Time (μs). Avoid ambiguous stacks of units. |
| Colorbars | State the physical quantity, units/normalization, ticks, and range. Comparisons use a shared norm; do not independently autoscale panels and imply relative strength. Explain out-of-range and missing values separately. |
| Whitespace | Reserve enough space for labels, colorbars, legends, and captions. Do not make a figure compact by clipping its edges. Panel spacing must first prevent axis-label collisions. |

Default canvas heights are illustrative choices. A double-column figure does not require proportionally larger text. If a figure is reduced after insertion into the manuscript, font sizes, line widths, and marker diameters all shrink and must be checked again.

## Left alignment and panel proportions in data figures

These general aesthetic defaults implement the user's requested style; they are not additional mandatory APS rules. They apply to single- and multipanel data figures, with scientific geometry and final-size readability taking priority.

- **Align the complete content bounding box with the text column.** Count the plotting area, y-axis titles, tick labels, scientific-notation offsets such as ×10⁻³, panel labels, and required legends/colorbars as visible content. Let the outermost necessary content define the figure's left boundary, retain a minimal safe margin against clipping, and bring that boundary close to the target column's left edge. Do not push the axes frame itself against the column edge. Keep space to the left of y-axis annotations compact; determine the safe margin from actual glyphs and exports, without a universal zero-whitespace rule.
- **Find the source of excess whitespace before correcting it.** If the file itself has an excessive left margin, adjust the canvas, axes layout, and label padding. If the file is already compact but is centered at an unnecessarily small insertion width, adjust its manuscript width/placement and recheck text sizes. If an exported PDF page contains large blank areas, correct its page box or export again from source. Changing only the caption or clipping y-axis text does not fix these problems. When cropping, retain all content and a safe margin, and recheck physical dimensions. Continue to honor this package's export contract: no silent tight cropping.
- **Align stacked figures using shared geometry.** For comparable stacked panels, prioritize aligned left/right plotting-area frames and a common reference line for y-axis titles. Allocate space for the longest ticks/titles and necessary colorbars. Tick labels of different widths naturally have different left edges; every text string need not align with the column edge. Preserve each scientific-notation offset's connection to its axis. Do not remove ticks, compress units, or move scientific annotations merely to fake alignment.
- **Keep bottom elements centered.** Center each x-axis title relative to its own plotting area. Center shared x-axis titles, bottom notes, and bottom legends relative to the panels or figure group they describe. Tightening the left side does not change these centering intentions. Manuscript-caption alignment and typesetting still follow the journal/template; this rule implies neither left-aligned nor centered captions.
- **Use near-square plotting areas by default for ordinary scalar plots.** Begin with reasonably near-square, unflattened axes boxes for ordinary curves, scatter plots, error bars, and small categorical plots, then refine for information density. Near-square refers to the plotting area's physical width and height, not the full canvas including labels, and need not mean exactly 1:1. Matplotlib's ax.set_box_aspect(1) is a possible starting point. It differs from ax.set_aspect('equal'), which constrains the ratio of x/y data units and must not be enabled solely for aesthetic reasons.
- **Allow nonsquare panels when the scientific task warrants them.** Preserve scientifically required aspect ratios for real-space/phase-space geometry or equal data-unit scales. Long time traces, dense spectra, many categories, or long category labels may genuinely require horizontal or vertical space; choose a wide or tall panel for readability and record why in the figure plan. Judge each plotting area separately in a stack. Do not force an entire stacked group into a square or stretch exported images to change their proportions.
- **Verify at the final insertion size.** After drawing/rendering, measure the bounding boxes of axes and all necessary labels. Check the left safety margin, panel-frame/y-title alignment, bottom-element centering, and each panel's width/height; then inspect the figure in the actual text column. Remove uninformative whitespace first, then choose appropriate canvas/column dimensions. Do not squeeze the layout by shrinking the 9 pt default text or sacrificing glyph height, subscripts, units, error bars, or colorbars. Checking the source canvas dimensions alone does not establish final-manuscript quality.

## Visual baseline for compact schematics

Use [schematic design](scheme-design.md) to establish actual objects and dependencies first. Compact high density is a user preference, subject to the final-size glyph and line-width checks above, with no additional node-count or fill-fraction target.

- **Shared visual language:** the same object retains its name, color, shape, and line-style identity in an overview, local detail, and data panel. Colors encode a limited set of semantic roles. Follow the [visual-brief method](scheme-design.md#turn-the-visual-method-into-a-brief-and-finished-artwork): use distinguishable role-based color fills on primary shapes, clear accent colors with dark outlines for central objects, and pale neutral backgrounds for supporting groups. Blue #4E79A7, orange #F28E2B, green #59A14F, and gray #6C757D are schematic starting points, without changing existing data-color meanings. Boundaries/text also identify frozen, trainable, or other states; color alone is insufficient.
- **Compact hierarchy:** panel labels, short module titles, and object labels each serve their own purpose. Put internal labels near operations/interfaces. Use pale backgrounds or thin boundaries for meaningful nesting. Large title bars, heavy containers, and repetitive legends must not overpower scientific structure.
- **Lines and endpoints:** the main path and central connections remain continuous and clear at final size. Repeated internal lines are lighter but traceable; supporting lines use distinct styles/labels. Choose specific widths from APS technical guidance and final readability rather than thickening every line. Leave room around interfaces and arrowheads; reserve short, continuous routing channels. Distinguish branches, merges, and crossings, and label the actual operation at each merge. Separate supervision/update lines clearly from forward data flow. Boundaries must not obscure line styles, and arrows must not pass through text.
- **Structure first:** as appropriate to the content, make network features/layers/connections or physical-platform components/controls/couplings/readout the main artwork, with nearby explanatory formulas and labels. Arranging correct terms and equations does not itself show structure. Independently compare the primary shapes and spatial organization with the user's visual reference.
- **Space budget:** compress uninformative padding, empty cards, repeated labels, and long arrows before changing panel proportions. Fit containers and canvas to actual content bounds and routing, retaining space required by labels and connections. Give a simple sequence only the height it needs; large titles and long vertical corridors should not pad a page. Inspect each large blank region: add source-supported mechanism structure if it is missing; otherwise tighten the layout. Do not fill gaps with unsupported detail. If more reading area is needed, use an appropriate double-column or layered layout rather than globally shrinking type to force a dense figure into one column.
- **Inspect at two scales:** first check the overall path and smallest glyphs at the final physical width. Zoom in to inspect endpoints, operators, subscripts, and nested boundaries, then return to final size. Readability under magnification does not establish final-size readability. Captions explain symbols but cannot repair missing key connections within the figure.

## Scope of the legacy four-journal examples: regressions, not a figure-selection entry point

The four old profiles preserve historical example sizes, not fixed journal aspect ratios. For new figures, [FIGURES](branch-figures.md) selects panels by scientific role, and the format references in [PLANNING](branch-planning.md) guide each figure's column width and height. The following describes only what the retained examples originally demonstrated:

- **PRL:** first make one key judgment readable within limited space. A compact main result with necessary controls may form a single-column stack, or span both columns to explain an experiment/mechanism. The prl_compact example is a two-panel vertical comparison; PRL does not require exactly two panels or single-column figures only.
- **PRA:** organize by method/protocol, parameter scan, or theory–numerical/experimental comparison. Clearly distinguish discrete data, reference curves, and errors. The pra_errorbars example demonstrates points, error bars, and a dashed reference; complex protocols can also span columns.
- **PRB:** spectra, momentum/energy maps, phase diagrams, and scaling relationships require comparable coordinates and color scales. Very simple single-column line plots also occur. The prb_heatmaps example uses matched ranges/colorbars; it does not establish a PRB preference for heatmaps.
- **PRX Quantum:** combine objects/protocols and performance evidence in layers for readers across quantum information and physics. When useful, put apparatus, circuit, or mechanism schematics beside quantitative figures. The prx_quantum_multipanel example is a four-panel performance comparison; neither four panels nor a wide figure is mandatory.

These are optional suggestions based on examples and article purposes, not frequency statistics. PRL's length constraint is a real editorial distinction; PRX Quantum Research Articles have no uniform length cap. Neither is a reason to reduce font sizes. [PRL](https://journals.aps.org/prl/authors) · [PRA](https://journals.aps.org/pra/authors) · [PRB](https://journals.aps.org/prb/authors) · [PRX Quantum](https://journals.aps.org/prxquantum/authors)

## Preserve scientific meaning

- Keep discrete observations at their original positions. Distinguish necessary connecting lines, fits, and theoretical curves. Smooth/resample only with a defined method and authorization; do not remove outliers, insert points, or alter data for appearance.
- Error bars/shaded bands must come from supplied data or an explicit method. State SD, SEM, CI, confidence level, n, and the independent/paired/repeated-measurement unit. Without error data, omit uncertainty marks; do not infer them from the appearance of a curve. All example uncertainties are manually specified values, not estimated intervals.
- Shared axes/colorbars in multipanel figures require comparable meanings. Clearly mark local enlargements and broken axes. Explain logarithmic scales, normalization, truncation, and aggregation in captions.
- Heatmap examples use interpolation='none' to retain the grid. Insufficient resolution does not authorize interpolation. Display or explain saturation when scalar values exceed vmin/vmax.

## Python use and delivery

Requires Python, NumPy, and Matplotlib. The examples were validated with NumPy 2.3.5 and Matplotlib 3.10.8. Do not install software or change user settings. Entry point: [aps_figure_style.py](../scripts/aps_figure_style.py). Runnable examples: [generate_figure_examples.py](../scripts/generate_figure_examples.py).

```bash
python scripts/generate_figure_examples.py --out assets/figure-examples
```

```python
import matplotlib.pyplot as plt
from scripts.aps_figure_style import style, size, export
with style():
    fig, ax = plt.subplots(
        figsize=size('pra', width_mm=85, height_mm=86), layout='constrained')
    ax.set_box_aspect(1)  # Near-square scalar-plot starting point, not equal data-unit scales
    ax.plot(x, y, '-o')  # x and y must come from actual research inputs
    ax.set(xlabel='Time (μs)', ylabel='Signal (arb. units)')
    export(fig, 'result')  # PDF + 600 dpi PNG, retaining the full physical canvas
```

Only the temporary style() context changes rcParams; importing does not change global settings. These dimensions and automatic layout are starting points. Adjust margins for actual long labels, legends, colorbars, and rendered bounding boxes, and check left whitespace after manuscript insertion. Profiles allow width/height overrides; they do not select data or statistics for the research task.

- Use PDF for manuscript assembly/vector archiving; pdf.fonttype=42 embeds TrueType fonts. Keep curves and text as vectors. Rasterize pixel content such as heatmaps selectively by artist; a screenshot of the whole figure is not a vector figure.
- The default PNG resolution is 600 dpi, explicitly a package quality choice. APS recommends plotting-software resolution of at least 600 dpi where possible. Do not invent a universal four-journal rule dividing outputs into 300/600/1200 dpi categories.
- export can explicitly use formats=('pdf','png','eps'). The package's EPS examples have no transparent layers. EPS does not support ordinary alpha transparency; figures with shaded regions need an appropriate color/transparency strategy and another check.
- **Separate submission from production:** new/revised submissions may use a combined PDF; source files are required after acceptance. APS Style Basics lists PS/EPS/JPG/PNG as preferred figure formats, and specifically mentions PS/EPS for the online-color/print-grayscale path. Do not describe the package's PDF output as the sole format accepted in every production workflow. [Submission guidance](https://journals.aps.org/authors/web-submission-guidelines-physical-review)
- The export function does not use bbox_inches='tight', avoiding silent changes to the complete 85/178 mm canvas. If cropping separately, remeasure final dimensions and fonts.

## Compact data tables

The graphical table example demonstrates appearance only. Deliver publication tables as editable LaTeX/REVTeX text, with captions above and Roman-numeral numbering. Define symbols/units and error meanings clearly. Use no vertical rules; use one horizontal rule below the header, with double rules at top and bottom as specified in the full APS guide. Align decimal places/precision and do not substitute table screenshots for source tables. An [editable table](../assets/figure-examples/compact_table.tex) is included.

## Examples and pre-delivery checks

The [overview PNG](../assets/figure-examples/style_overview.png) is for comparison only, not a manuscript figure. The five groups of original-size PNG/PDF and EPS files and their caption notes use explicitly labeled synthetic data. In actual research figures, replace the Synthetic example note with real provenance information or remove it as appropriate; never use example numbers as paper results.

Schematics must first pass the [content and relationship checks](scheme-design.md#final-artwork-checks-visible-and-explainable-relationships). Correct styling does not establish that scientific relationships are visible.

Check actual figures for final insertion size; the left content boundary including y-axis annotations; each plotting area's proportions and bottom-element centering, following the layout rules above; smallest glyphs/subscripts; marker diameters and line widths; legend/colorbar clipping; black-and-white and color-vision distinguishability; error meanings; each panel's quantities/units; font embedding; selective raster layers; and reproducibility. Use final-size PDF pages or 100% printouts. Browser-zoom screenshots are supplementary only.

The [public provenance record](../docs/PROVENANCE.md) describes the official-requirement checks, visual sampling, and technical validation behind this reference. For axis-label conventions, see [APS Axis Labels and Scales](https://journals.aps.org/authors/axis-labels-and-scales-on-graphs-h18); for full table and typesetting guidance, see the [APS Journals Style Guide](https://res.cloudinary.com/apsphysics/image/upload/APS_Journals_Style_Guide_Authors022326_guzwhx.pdf).
