# FIGURES: decide what a figure establishes before deciding how it looks

Use this branch for scientific figure planning and Python plotting. Whole-manuscript figure placement, column widths, and page budgets belong to [PLANNING](branch-planning.md) and its final-format references. For fonts, lines, output formats, and statistical integrity, read the [technical figure style baseline](figure-style.md). Without data, deliver a figure design rather than fabricated research results.

## From a claim to discriminating evidence

For every figure, first ask: What physical judgment should it establish? Which two explanations, regimes, or predictions must the reader distinguish? What data are available, and what is missing? Choose quantities, controls, and coordinates accordingly, rather than defaulting to mean-value scatter plots for every parameter.

| Scientific task | Suitable evidence geometry | Required inputs and limits |
|---|---|---|
| Identify interference, hybridization, resonances, or mode structure | Spectra/complex poles, frequency response, avoided crossings, or phase response, with uncoupled or detuned controls | Actual spectra, a model, or complex amplitudes; an intensity curve alone may not distinguish mechanisms |
| Distinguish transients, transport, and steady states | Time traces, space-time maps, impulse responses, or correlation functions, with varied initial states/controls | Time-resolved data, time units, and control conditions; do not reconstruct trajectories from means |
| Identify state structure or fluctuations | Distributions, histograms, state-space or Wigner plots, or joint distributions | Raw samples or a valid state reconstruction with its method; mean error bars cannot stand in for missing distribution data |
| Test scaling laws and phase boundaries | Raw curves for multiple sizes, scaling collapse, phase diagrams with representative cuts, or theoretical asymptotes | Multiple sizes/ranges and a fitting basis; a fit to a few points does not automatically establish a limiting law |
| Separate a mechanism from alternative explanations | The same observable under controlled mechanism-on/off conditions, residuals, or differences | Actual controls or a reproducible model; state which variables change together |
| Compare theory, algorithms, or measurement precision | Error, bound, or performance curves, discrete points, and necessary uncertainties | Means/scatter may be exactly appropriate; do not replace them with unsupported heatmaps merely for variety |

A finite-size trend is not a scaling collapse; spectral collapse is not data collapse; deterministic time evolution is not a stochastic single-shot trajectory; a Wigner quasiprobability is not an ordinary sample histogram. Name the actual data object instead of substituting visually similar evidence.

For mechanisms, apparatus, protocols, inference/calibration workflows, or revisions prompted by an overly simple schematic, read [schematic design](scheme-design.md). First map the paper's objects, variables, conditions, and central relationships into visible structure. Then write the six-part visual brief: layout, object shapes, role-based colors, details, connections, and labels/dimensions. Give key scientific objects distinct color fills, reserve pale backgrounds for grouping, and organize connections by importance. Check each choice in the rendered result. The design reference gives the execution method; a colored wireframe does not by itself implement that method. The default is a compact, layered, readable journal schematic: label what passes along the main path, expose internal operations and intermediate objects in key modules, and use any necessary mechanism detail to add information rather than duplicate the overview. Density comes from efficient use of space and real relationships, not smaller text or unsupported structures. This is a user preference, not a universal APS requirement. A chain of method names or generic icons does not automatically explain a mechanism; neither node counts nor panel counts are complexity targets. When neural methods are relevant, make inputs/features, source-supported network layers and connections, latent quantities, and outputs structurally visible. When a physical implementation is relevant, connect actual components/degrees of freedom, controls, couplings, and readout to computational signals. Select these representations conditionally from the paper: lettered boxes cannot stand in for networks, operation circuits cannot stand in for requested hardware, and irrelevant papers need neither. A mechanism schematic expresses model, pathway, or apparatus relationships; it cannot replace quantitative evidence. Curves, heatmaps, schematics, spectra, and distributions may coexist, or a figure set may use just one type if it answers the question most directly.

## A figure set is not a uniform panel grid

Arrange the main result, mechanism/control, range of applicability, and synthesis in reading order. One figure may serve several of these roles; there is no one-role-per-figure requirement. Choose dominant panels and secondary validation panels. Place the most important comparisons next to each other with comparable coordinates, but do not force unlike data to share axes.

- Default to near-square plotting areas for ordinary scalar curves, scatter plots, error bars, and small categorical plots; avoid unjustifiably flat panels. This describes each axes box's physical shape, not the whole canvas or an equal ratio of data units.
- Long time traces, dense spectral scans, broad phase diagrams, or numerous categories/long labels may genuinely need wide or tall panels. Record the reason in the figure plan.
- Two-dimensional correlation/phase-space plots and plots with symmetric coordinates often suit near-square panels; the data's geometry determines the coordinate aspect ratio.
- A dominant heatmap with a few parameter cuts, or an apparatus/pathway plus response and control, can use unequal-width GridSpec layouts to establish a clear hierarchy.
- Single-column vertical stacks suit related results with a clear sequence and readable axis text. Complex mechanism comparisons or long axis labels may work better across both columns.
- A manuscript may mix wide, square, and composite figures, with no quota for any shape. If every figure has exactly the same size/layout, check that the scientific task, rather than a default template, actually justifies it.

Follow [left alignment and panel proportions](figure-style.md#left-alignment-and-panel-proportions-in-data-figures) to reduce uninformative space to the left of y-axis annotations, bringing the complete figure content close to the text column's left edge. Align stacked panel frames and y-axis titles sensibly while retaining safe margins. Center x-axis titles, shared bottom titles, and bottom notes/legends within their respective reference areas. Manuscript captions still follow the journal template. Check the near-square default and its scientific exceptions panel by panel; do not compress an entire figure group into a square.

Keep color identities, fonts, line styles, panel labels, and units consistent while retaining necessary differences in aspect ratio and panel size. Balance means that visual weight matches evidential importance, not that all shapes receive equal space.

## Keep structure, process, and quantitative tests close together

When structure affects performance, place components next to their response, sensitivity, or error diagnostics. When explaining a protocol, encoding, or inference workflow, track the same scientific object through successive stages wherever possible, preserving corresponding positions, symbols, and colors. Reuse comparable axes and normalization for controls, adding actual residuals or differences when needed. This increases information density and reduces the work of finding correspondences across figures.

Specific examples from the three added journals support these practices; see the [additional evidence ledger](evidence-ledger-v12.md) and each journal profile. Caption-only review supports judgments about scientific roles; conclusions about color, spatial organization, and actual readability are limited to samples explicitly recorded as visually inspected. Small diagnostics next to components may use proportions suited to the comparison; still check the near-square default and scientific exceptions for each main data panel.

## A short plan to record before plotting

For each figure, write one line or a short paragraph: claim → available data → discriminating comparison → figure type/panel hierarchy → single- or double-column placement and intended width/height → first discussion in the text. Identify any missing data. Do not generate an attractive figure first and invent its mechanism afterward.

The same research data may support different presentations, but do not smooth away structure, selectively truncate ranges, change statistical units, or manufacture uncertainty. Captions must distinguish data, calculations, schematics, and fits. See the [technical baseline](figure-style.md) for detailed requirements.

## The provenance chain from data to panel

Reuse existing records and retain a minimal reproducible chain for every panel: data file/version → columns or arrays and units → filtering, aggregation, normalization, and fitting methods → script/parameters → figure file and caption. Distinguish measured data, simulations actually computed from the specified model, theoretical curves, conceptual schematics, and mock values used only for layout. Simulations with documented methods and computational provenance can be research evidence; arbitrary placeholder numbers cannot.

Choose carefully for the scientific task: use curves for continuous evolution while preserving sampling identity; prefer points with actual uncertainty for discrete estimates; use scatter, predictions, and necessary residuals for association/model tests; distributions require samples and sample sizes; two-dimensional fields require grids, masks, and meaningful color scales; a table may suit a few precise values. Identify errors as SD, SEM, CI, systematic error, or fitting uncertainty, and state their calculation basis. Report numerical convergence errors separately. If only means are supplied, do not reverse-engineer samples, confidence bands, or density shapes.

If data or essential definitions are missing, provide an executable design and precise gaps, and continue with the parts that can be drawn. When inputs and tools are complete, generate the figures, inspect the finished output, and correct it; figure-type suggestions or prompts do not replace final artwork. Schematics and data figures share symbol/color identities while retaining their own scientific meanings. Schematics also require a content check: inputs, constraints/transformations, and outputs must be traceable; the main artwork must visibly show the paper's specific relationships; fixed/varying objects, measured/inferred quantities, and exact/approximate conditions must remain distinct. Check these relationships in the final-size rendering; accurate language in a plan cannot replace rendering validation. Assess scientific meaning/rendering separately from matching the user's visual reference. The latter requires an actual comparison of structural representation and spatial organization; technical success does not automatically mean stylistic success.

## Runnable examples and adaptation

The [mechanism example script](../scripts/generate_mechanism_examples.py) uses an explicitly synthetic two-mode linear model to generate a double-column response map with spectral cuts, a near-square pole trajectory, and a wide dynamics figure. These are not paper results or a template requiring all three figures. Mechanism-related parameters are computed by the script, not guessed from appearance.

Choose footprint and height_mm explicitly for each figure; do not let a PRL/PRA/PRB label determine the aspect ratio automatically. Older examples remain as basic style regressions, not the default figure set for a new paper. Historical scripts and assets demonstrate technical styling and export interfaces; new layouts follow the current scientific objects and the user's visual references rather than inheriting sparse geometry from minimal demonstrations. Run:

```bash
python scripts/generate_mechanism_examples.py --out assets/mechanism-examples
```

Deliver PDF/PNG figures at their final physical dimensions, a reproducible script, data provenance, and captions. Check scaled glyphs, boundary/legend clipping, grayscale distinguishability, shared color scales, and normalization. Claim that appearance was checked only after actually generating and inspecting the rendered figures.

Pixel-level review of nine additional published PRL PDFs supports assigning layouts by scientific role; see the [public provenance record](../docs/PROVENANCE.md). These are limited observations, not APS requirements, and do not count the entire 400-paper archive as visually reviewed.
