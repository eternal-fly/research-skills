# Figure planning record: a physical question with a checkable evidence layout

Use this record before making a new figure or substantively reorganizing one. For a local label correction, reuse the established record rather than reopening every decision. This is an editorial interface, not an APS form and not evidence that the underlying science is correct.

## Decide the scientific comparison before assigning panel roles

State the supported physical judgment and the explanations, regimes, predictions, or resource models that must be distinguished. If there is no competing explanation, state the actual comparison or definition instead. Identify the observable and controls that discriminate between them. Only then assign panels. A validation panel earns trust in a specific inference; a decorative apparatus picture does not.

Use the same fixed fields for a small one-panel plot and a large figure set. Values may be short. Record `not applicable: <reason>` when a field is genuinely irrelevant and `missing: <needed input>` when it blocks a conclusion. Do not fill fields with guessed data, uncertainties, controls, or mechanisms. Reuse existing metadata and transformation records by reference rather than duplicating them.

## Fixed record

**Figure-level fields**

1. Figure identifier and status: draft or ready for delivery.
2. Supported claim and its decisive conditions.
3. Discriminating question: alternatives or regimes to distinguish, and what would count against the claim.
4. Evidence sequence: how the panels jointly support the claim, without inventing a causal or proof dependency.
5. Panel records, in intended reading order (fields below).
6. Main-text location and space budget: first substantive discussion, journal/article type, target width and height.
7. Column decision: start with single column; record the outcome of the single-column check, chosen width, and reason for any change.
8. Visual semantics: identities of objects, colors, markers, lines, color-scale direction/normalization, and panel-label placement; preserve these across the same work and document any justified change.
9. Open scientific or visual checks and delivery artifacts.

**Each panel has these fields**

- Identifier; local claim; primary role, with optional secondary roles.
- Observable and units/normalization; model/system, parameters, initial state, sampling unit, and approximation conditions needed for interpretation.
- Source kind: measurement, simulation, theoretical calculation, schematic, or layout-only mock.
- Raw source/version or defining model; processed data/arrays; selection, filtering, aggregation, normalization or fit; generating script and parameters. Link to existing records where available.
- Comparator/control and whether resources, data splits, axes, and normalization are matched.
- Uncertainty: definition, independent sample count/unit and calculation basis, numerical convergence or systematic contribution, or justified non-applicability. A deterministic theorem does not need invented error bars.
- Principal challenge: what alternative interpretation or missing evidence could invalidate this panel's inference; distinguish a scientific limitation from an unrelated unperformed extension.
- Intended visual encoding and relation to neighboring panels.

The optional [JSON template](../assets/planning/figure-plan.template.json) carries these fields for reusable workflows. The [record validator](../scripts/validate_figure_plan.py) checks structural completeness, journal/article-type presence, explicit unresolved template sentinels, and selected readiness inconsistencies; it does not inspect source data, judge claims, enforce all prose rules, or certify visual readability. A Markdown record using the same fields is equally acceptable.

## Panel roles: labels for reasoning, not a quota

- **Orientation:** define the system, observable, protocol, geometry or resource model needed to interpret later evidence.
- **Validation:** establish a particular calibration, baseline, convergence result or known-limit reproduction.
- **Finding:** present the decisive observable, bound, scaling, comparison or capability.
- **Explanation:** distinguish a proposed mechanism or connect the result to a physical or mathematical structure, using actual supporting evidence.
- **Limits:** show relevant uncertainty, finite-size/parameter domain, cost, failure mode, or alternative that changes interpretation.

These role names are a planning vocabulary, not published panel labels. Not every paper needs every role. A panel can have a primary and secondary role; one figure can combine several roles. Keep independent complementary evidence when it adds necessary information, even if the plotted observable is the same. Merge redundant panels, not distinct tests of a shared claim. Purely analytical work can need no data plot at all.

## Single-column first, with an explicit escape test

Use the user's specified format when given. Otherwise start at the target template's single-column width and preserve the existing near-square default for ordinary scalar plotting areas. Do not equate single column with a square whole figure, one panel, or vertical-only organization.

Before accepting that width, check:

1. **Inference:** are the essential comparison, coupled mechanism, paths and shared variables visible together without breaking the argument into disconnected fragments?
2. **Reading:** at the final insertion size, do glyphs, subscripts, data, uncertainties, ticks and colorbars remain legible and unclipped?
3. **Geometry:** do state-space maps, dense spectra, long time traces and necessary aspect ratios retain their meaning?
4. **Economy:** can redundant labels, padding or genuine duplicate evidence be removed without hiding conditions or reducing the comparison?

If single column passes, keep it. If it fails after reasonable layout repair, use double column or another authorized template width and record which test failed. A wide figure can be necessary for two coupled panels, while four panels may fit one column. Never determine width from panel count alone, shrink type to force compliance, split a coupled mechanism merely to stay narrow, or add unsupported panels to fill a wide canvas. Recheck the final exported and inserted figure after changing width. The two-column example width in the package is a working preset, not a substitute for the manuscript's actual text width.

## Quantum-domain recipes are conditional evidence routes

Use [quantum figure recipes](quantum-figure-recipes.md) only for relevant scientific tasks. Start with the physical question, test its input requirements, and adapt the record rather than collecting all suggested panels. The [reread evidence record](../evidence/quantum-figure-review/README.md) distinguishes fresh targeted text/caption reads, actual image inspection, inherited metadata, and inaccessible sources. A recipe does not authorize new experiments or computations; request missing scientific inputs or mark the blocked inference.
