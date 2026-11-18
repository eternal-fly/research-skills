# Visual forms and palette collections

Marks, color and layout are independent choices. Present a general menu by mark, scale or layout. Reserve study-specific design choices for work on a supplied dataset or manuscript. An existing manuscript's visual identities can carry through a revision. The data provide the coordinates, sampling units and normalization for any selected form.

## Visual forms

| Family | Available forms | What the marks encode |
|---|---|---|
| Points and intervals | Dot strip, jittered strip, paired marks, point with whiskers | A point retains one observation or estimate. A segment links a known pair. Whisker endpoints carry a defined interval. |
| Bars and proportions | Horizontal or vertical bars, grouped bars, stacked bars | Length from a common zero carries magnitude. Segments in a normalized stack share a stated denominator. |
| Ordered traces | Line, line with markers, step, trace with ribbon | Position orders the observations. An interruption can mark a gap. The ribbon has a stated calculation or interval. |
| Distributions | Empirical cumulative steps, histogram, box with points, density outline, violin, ridgeline | A step counts observations, a bin counts or normalizes them and an outline estimates a density. Give sample size, bin edges or bandwidth as applicable. |
| Joint coordinates | Scatter, small multiples, hexagonal bins, marginal strips | Position carries two values on the same observation. A bin can carry count or density. Margins summarize the same sample. |
| Cells and fields | Annotated matrix, clustered matrix, continuous field, contours, marked cuts | Cells retain row and column identities or physical coordinates. Masks, shared limits and units identify the scale. A cut uses the recorded coordinates of the displayed array. |
| Connections | Paired segments, weighted ribbons, labeled nodes and edges | Edges require observed links or a specified model. Varying ribbon width represents a joint weight; separate marginal totals support only the endpoint displays. |
| Layers and panels | Reference line, labeled window, categorical strip, aligned marginal, inset, shared axes, unequal panel widths | An overlay or adjacent panel can carry an independent quantity. Give each encoding a key and keep shared quantities on comparable axes. |

## Color collections

The original five-color cycle is blue `#0072B2`, vermilion `#D55E00`, green `#009E73`, purple `#CC79A7` and ink `#222222`. It remains the default of the plotting style. Both collections below can be selected by name. Colors identify visual roles independently of the choice of mark.

| Color structure | Original collection | Additional collection |
|---|---|---|
| Nominal colors and matching tints | `aps-cycle` | `class-identity`, `condition-pair`, `cohort-distributions`, `trace-pair` |
| Ordered lightness | `cividis` | `magnitude-blue`, `feature-order` |
| Opposing values around a neutral point | `RdBu_r` | `signed-balance` |
| Accent or background layers | | `focus-context`, `epoch-windows` |
| Closed cycle | | `wrapped-phase` |

Keep nominal identities stable across linked panels and give them a shape, dash or label where needed. Mark the neutral value on a diverging scale, both endpoints on a periodic scale, and missing values separately. Shared colorbars use the same normalization. At final width, check the thinnest stroke and the lightest fill in context.

The [catalog](../assets/data-palettes.json) lists both collections, role colors and scalar-scale definitions. The [schematic collection](schematic-palettes.md) retains its ten families and Floquet preset. The [gallery](../assets/data-figures/gallery.pdf) illustrates the visual forms with synthetic coordinates. Its final page compares original and additional scales on identical arrays.

## Using a named option

The [plotting style module](../scripts/aps_figure_style.py) exposes the original and additional palettes through the same functions. `data_palette()` returns the original cycle. `data_palette(name)` returns the requested role colors or scalar definition. `data_colormap(name)` returns an independent Matplotlib scalar colormap. An explicit choice is local to the artist using it. The `style()` context retains its original defaults.

```python
from aps_figure_style import data_colormap, data_palette

original = data_palette('aps-cycle')['colors']
additional = data_palette('class-identity')['colors']
original_scale = data_colormap('cividis')
additional_scale = data_colormap('magnitude-blue')
```

From the skill root, run `python scripts/draw_data_figures.py --out gallery.pdf` to reproduce the [English gallery](../assets/data-figures/gallery.pdf). The scalar-scale definitions follow the [Matplotlib colormap guide](https://matplotlib.org/stable/users/explain/colors/colormaps.html).
