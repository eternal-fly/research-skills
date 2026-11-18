"""Render the English visual-form and palette gallery with synthetic data."""
import argparse
from datetime import datetime, timezone
from pathlib import Path

import matplotlib as mpl

mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.patches import PathPatch, Rectangle
from matplotlib.path import Path as Curve
import numpy as np

from aps_figure_style import data_colormap, data_palette, style

INK = '#283946'
SECONDARY = '#4D606C'


def page(title, height=126):
    fig = plt.figure(figsize=(178 / 25.4, height / 25.4))
    fig.text(0.057, 0.963, title, va='top', fontsize=14, weight='semibold', color=INK)
    return fig


def footer(fig, text):
    fig.text(0.057, 0.024, text, va='bottom', fontsize=8, linespacing=1.3, color=SECONDARY)


def label(ax, text):
    ax.set_title(text, loc='left', fontsize=9.5, weight='semibold', pad=5, color=INK)
    ax.spines[['top', 'right']].set_visible(False)


def swatch(fig, x, y, key):
    spec = data_palette(key)
    fig.text(x, y, spec['name'], color=INK, fontsize=9.2, weight='semibold')
    fig.text(x, y - 0.023, key, color=SECONDARY, fontsize=8)
    ax = fig.add_axes([x, y - 0.051, 0.376, 0.015])
    if spec['kind'] in ('sequential', 'diverging', 'cyclic'):
        ax.imshow(
            np.linspace(0, 1, 257)[None, :],
            cmap=data_colormap(key),
            aspect='auto',
            interpolation='nearest',
            extent=(0, 1, 0, 1),
        )
    else:
        colors = list(spec['colors'].values())
        ax.barh(
            [0.5] * len(colors),
            1 / len(colors),
            left=np.arange(len(colors)) / len(colors),
            height=1,
            color=colors,
            edgecolor='white',
            linewidth=0.55,
        )
    ax.set(xlim=(0, 1), ylim=(0, 1))
    ax.axis('off')


def palette_page():
    fig = page('Palette collections', height=163)
    left, right = 0.065, 0.555
    for x, heading in [(left, 'Original collection'), (right, 'Additional collection')]:
        fig.text(x, 0.858, heading, color=SECONDARY, fontsize=10.4)
    pairs = [
        ('aps-cycle', 'class-identity'),
        ('cividis', 'magnitude-blue'),
        ('RdBu_r', 'signed-balance'),
    ]
    for i, (original, additional) in enumerate(pairs):
        y = 0.814 - i * 0.103
        swatch(fig, left, y, original)
        swatch(fig, right, y, additional)
    fig.text(left, 0.485, 'Additional mark and scale options', color=SECONDARY, fontsize=10.4)
    keys = [
        'condition-pair',
        'cohort-distributions',
        'trace-pair',
        'focus-context',
        'epoch-windows',
        'feature-order',
        'wrapped-phase',
    ]
    for i, key in enumerate(keys):
        swatch(fig, left if i % 2 == 0 else right, 0.443 - (i // 2) * 0.098, key)
    footer(fig, 'Names below the swatches are the keys used in the palette catalog.')
    return fig


def four_panels(title):
    fig = page(title, height=136)
    axes = fig.subplots(2, 2)
    fig.subplots_adjust(left=0.13, right=0.96, bottom=0.165, top=0.815, wspace=0.52, hspace=0.99)
    return fig, axes.ravel()


def marks_page():
    fig, (points, bars, pairs, trace) = four_panels('Marks and intervals')
    original = data_palette()['colors']
    tones = data_palette('condition-pair')['colors']
    series = np.array(
        [
            [0.30, 0.39, 0.42, 0.47, 0.51],
            [0.48, 0.50, 0.55, 0.57, 0.62],
            [0.34, 0.42, 0.47, 0.51, 0.57],
        ]
    )
    levels = np.arange(3)
    names = ['A', 'B', 'C']
    center = series.mean(axis=1)
    low, high = np.quantile(series, [0.2, 0.8], axis=1)
    label(points, '(a)  Points and intervals')
    points.errorbar(
        center, levels, xerr=[center - low, high - center], fmt='o', color=original['blue'], capsize=3
    )
    points.set(yticks=levels, yticklabels=names, ylim=(2.6, -0.6), xlim=(0.2, 0.7), xlabel='Value')
    label(bars, '(b)  Bars')
    bars.barh(levels, center, color=original['blue'], height=0.55)
    bars.set(yticks=levels, yticklabels=names, ylim=(2.6, -0.6), xlim=(0, 0.7), xlabel='Mean value')
    label(pairs, '(c)  Paired marks')
    values = np.column_stack((series[0], series[1]))
    for a, b in values:
        pairs.plot([0, 1], [a, b], color=tones['pair_link'], linewidth=0.9)
    pairs.scatter(
        np.zeros(len(values)),
        values[:, 0],
        s=17,
        marker='o',
        facecolor='white',
        edgecolor=tones['control'],
        zorder=3,
    )
    pairs.scatter(
        np.ones(len(values)),
        values[:, 1],
        s=17,
        marker='s',
        facecolor='white',
        edgecolor=tones['intervention'],
        zorder=3,
    )
    pairs.set(
        xlim=(-0.22, 1.22), ylim=(0.24, 0.68), xticks=[0, 1], xticklabels=['A', 'B'], ylabel='Value'
    )
    label(trace, '(d)  Lines and bands')
    t = np.linspace(0, 1, 70)
    curves = np.array(
        [
            0.2 + 0.45 * t + offset * (0.45 + 0.35 * np.sin(np.pi * t))
            for offset in np.linspace(-0.13, 0.13, 15)
        ]
    )
    interval = np.quantile(curves, [0.1, 0.9], axis=0)
    trace.fill_between(t, *interval, color=tones['intervention_band'])
    trace.plot(t, np.median(curves, axis=0), color=tones['intervention'], linewidth=1.45)
    trace.set(xlim=(0, 1), ylim=(0.1, 0.78), xticks=[0, 0.5, 1], xlabel='Coordinate', ylabel='Value')
    footer(
        fig,
        'Synthetic values. Whiskers span the 20th to 80th percentiles. The band spans the 10th to 90th percentiles.',
    )
    return fig


def distribution_page():
    fig, (strip, steps, cloud, bins) = four_panels('Distributions and joint coordinates')
    rng = np.random.default_rng(328)
    values = [rng.normal(-0.25, 0.65, 35), rng.normal(0.38, 0.85, 35)]
    colors = data_palette('trace-pair')['colors']
    for j, (sample, role, mark, ls) in enumerate(
        zip(values, ['teal', 'berry'], ['o', 's'], ['-', '--'])
    ):
        strip.scatter(
            sample,
            j + rng.uniform(-0.14, 0.14, len(sample)),
            s=12,
            marker=mark,
            facecolors='white',
            edgecolors=colors[role],
            linewidth=0.65,
        )
        xs = np.sort(sample)
        steps.step(
            np.r_[-3, xs, 3],
            np.r_[0, np.arange(1, len(xs) + 1) / len(xs), 1],
            where='post',
            color=colors[role],
            ls=ls,
            label=['A', 'B'][j],
            linewidth=1.25,
        )
    label(strip, '(a)  Dot strips')
    strip.set(yticks=[0, 1], yticklabels=['A', 'B'], ylim=(1.6, -0.6), xlim=(-3, 3), xlabel='Value')
    label(steps, '(b)  Empirical steps')
    steps.set(xlim=(-3, 3), ylim=(-0.04, 1.04), yticks=[0, 0.5, 1], xlabel='Value', ylabel='Fraction')
    steps.legend(loc='lower right', fontsize=8)
    x = rng.normal(size=700)
    y = 0.55 * x + rng.normal(0, 0.8, len(x))
    label(cloud, '(c)  Scatter')
    cloud.scatter(x, y, s=7, color=data_palette()['colors']['blue'], alpha=0.48, linewidth=0)
    label(bins, '(d)  Hexagonal counts')
    image = bins.hexbin(x, y, gridsize=19, mincnt=1, cmap=data_colormap('cividis'), linewidths=0)
    fig.colorbar(image, ax=bins, fraction=0.055, pad=0.045).ax.set_title('n', fontsize=8, pad=3)
    for ax in (cloud, bins):
        ax.set(
            xlabel='x', ylabel='y', xlim=(-4, 4), ylim=(-4, 4), xticks=[-3, 0, 3], yticks=[-3, 0, 3]
        )
    footer(
        fig,
        'Synthetic samples. The two dot strips and their steps use the same 35 values per group.\nThe two lower panels share 700 coordinate pairs and the same axis limits.',
    )
    return fig


def flow_panel(ax, counts, colors):
    gap = 8
    left_totals, right_totals = counts.sum(axis=1), counts.sum(axis=0)
    left = np.r_[0, np.cumsum(left_totals[:-1] + gap)]
    right = np.r_[0, np.cumsum(right_totals[:-1] + gap)]
    source, target = left.copy(), right.copy()
    for i, row in enumerate(counts):
        for j, w in enumerate(row):
            a, b = source[i], target[j]
            verts = [
                (0, a),
                (0.45, a),
                (0.55, b),
                (1, b),
                (1, b + w),
                (0.55, b + w),
                (0.45, a + w),
                (0, a + w),
                (0, a),
            ]
            codes = [
                Curve.MOVETO,
                *[Curve.CURVE4] * 3,
                Curve.LINETO,
                *[Curve.CURVE4] * 3,
                Curve.CLOSEPOLY,
            ]
            ax.add_patch(
                PathPatch(
                    Curve(verts, codes), facecolor=colors[i], edgecolor='white', lw=0.45, alpha=0.49
                )
            )
            source[i] += w
            target[j] += w
    for side, starts, totals in [(0, left, left_totals), (1, right, right_totals)]:
        for name, c, start, total in zip('ABC', colors, starts, totals):
            ax.add_patch(Rectangle((side - 0.014, start), 0.028, total, facecolor=c))
            ax.text(
                side + (-0.04 if side == 0 else 0.04),
                start + total / 2,
                name,
                va='center',
                ha='right' if side == 0 else 'left',
            )
    end = counts.sum() + gap * (len(counts) - 1)
    ax.set(xlim=(-0.16, 1.16), ylim=(end + 4, -4))
    ax.axis('off')


def layers_page():
    fig, (cells, flow, lines, cycle) = four_panels('Cells, layers and connections')
    counts = np.array([[40, 15, 5], [12, 20, 8], [8, 5, 7]])
    label(cells, '(a)  Annotated cells')
    cells.imshow(
        counts, cmap=data_colormap('magnitude-blue'), vmin=0, vmax=40, interpolation='nearest'
    )
    for (i, j), v in np.ndenumerate(counts):
        cells.text(
            j, i, str(v), ha='center', va='center', color='white' if v > 27 else INK, fontsize=8.4
        )
    cells.set(xticks=range(3), xticklabels=list('ABC'), yticks=range(3), yticklabels=list('ABC'))
    label(flow, '(b)  Weighted ribbons')
    nominal = data_palette('class-identity')['colors']
    flow_panel(flow, counts, [nominal[k] for k in ['blue', 'orange', 'green']])
    label(lines, '(c)  Interval backgrounds')
    layer = data_palette('epoch-windows')['colors']
    x = np.linspace(0, 1, 150)
    lines.axvspan(0.12, 0.36, color=layer['drive_window'], lw=0)
    lines.axvspan(0.57, 0.83, color=layer['recovery_window'], lw=0)
    lines.plot(x, 0.2 + 0.55 * x + 0.11 * np.sin(4 * np.pi * x), color=layer['signal'])
    for pos, txt in [(0.24, 'I'), (0.70, 'II')]:
        lines.text(pos, 0.89, txt, transform=lines.transAxes, ha='center', fontsize=8, color=INK)
    lines.set(xlim=(0, 1), ylim=(0, 1), xticks=[0, 0.5, 1], xlabel='Coordinate', ylabel='Value')
    label(cycle, '(d)  Cyclic field')
    x = np.linspace(-1, 1, 121)
    u, v = np.meshgrid(x, x)
    angle = np.ma.array(np.arctan2(v, u), mask=np.hypot(u, v) < 0.08)
    im = cycle.imshow(
        angle,
        origin='lower',
        extent=(-1, 1, -1, 1),
        cmap=data_colormap('wrapped-phase'),
        vmin=-np.pi,
        vmax=np.pi,
        interpolation='nearest',
    )
    cycle.set(xticks=[-1, 0, 1], yticks=[-1, 0, 1], xlabel='x', ylabel='y')
    cb = fig.colorbar(im, ax=cycle, fraction=0.055, pad=0.045, ticks=[-np.pi, 0, np.pi])
    cb.ax.set_yticklabels(['−π', '0', 'π'])
    footer(
        fig,
        'Synthetic values. Each ribbon width equals its corresponding cell count. The periodic field is masked at the center.',
    )
    return fig


def scalar_page():
    fig = page('Same coordinates, two palettes', height=129)
    x = np.linspace(-1, 1, 121)
    u, v = np.meshgrid(x, x)
    fields = [
        np.exp(-4 * (u - 0.35 * v) ** 2 - 2 * v**2),
        np.sin(np.pi * u) * np.cos(0.5 * np.pi * v),
    ]
    options = [('cividis', 'magnitude-blue'), ('RdBu_r', 'signed-balance')]
    fig.text(0.212, 0.855, 'Original collection', color=INK, weight='semibold', fontsize=9.6)
    fig.text(0.65, 0.855, 'Additional collection', color=INK, weight='semibold', fontsize=9.6)
    for i, (field, keys) in enumerate(zip(fields, options)):
        lower = [0.54, 0.19][i]
        for j, key in enumerate(keys):
            ax = fig.add_axes([[0.112, 0.56][j], lower, 0.265, 0.244])
            im = ax.imshow(
                field,
                origin='lower',
                extent=(-1, 1, -1, 1),
                cmap=data_colormap(key),
                vmin=[0, -1][i],
                vmax=1,
                interpolation='nearest',
                aspect='auto',
            )
            ax.set(xticks=[-1, 0, 1], yticks=[-1, 0, 1], ylabel='y', xlabel='x' if i else '')
            ax.set_title(key, fontsize=8.6, pad=4)
            cb = fig.colorbar(
                im,
                cax=fig.add_axes([[0.394, 0.842][j], lower + 0.018, 0.013, 0.208]),
                ticks=[[0, 0.5, 1], [-1, 0, 1]][i],
            )
            cb.ax.tick_params(labelsize=8)
    footer(
        fig,
        'Synthetic coordinates. Each row uses the same array, limits and normalization in both columns.',
    )
    return fig


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True, help='Destination PDF')
    out = parser.parse_args().out
    out.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime(2026, 11, 18, tzinfo=timezone.utc)
    with style(), PdfPages(
        out,
        metadata={
            'Title': 'Visual forms and palette collections',
            'Author': 'APS Quantum Writing',
            'CreationDate': stamp,
            'ModDate': stamp,
        },
    ) as pdf:
        for make in [palette_page, marks_page, distribution_page, layers_page, scalar_page]:
            fig = make()
            pdf.savefig(fig, dpi=300)
            plt.close(fig)


if __name__ == '__main__':
    main()
