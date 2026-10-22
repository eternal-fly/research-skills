"""Synthetic analytic figure smoke test; no measured or simulated research data."""
import csv
import json
from pathlib import Path
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
from aps_figure_style import style, export


def generate(out):
    out.mkdir(parents=True, exist_ok=True)
    p = np.linspace(0, .45, 451)
    overhead = 1 / (1 - 2*p)**2
    samples = np.array([.05, .10, .20, .40])
    expected = np.array([1.2345679012, 1.5625, 2.7777777778, 25.0])
    np.testing.assert_allclose(1/(1-2*samples)**2, expected, rtol=1e-10)
    with (out / 'values.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f); writer.writerow(['p', 'variance_overhead'])
        writer.writerows(zip(p, overhead))
    with style():
        fig = plt.figure(figsize=(85/25.4, 76/25.4))
        ax = fig.add_axes([.22, .20, .73, .75])
        ax.plot(p, overhead, color='#0072B2')
        ax.scatter(samples, 1/(1-2*samples)**2, s=18, facecolors='white',
                   edgecolors='#0072B2', zorder=3)
        ax.axhline(1, color='#222222', linestyle='--', linewidth=.8)
        ax.set(xlabel='Bit-flip probability $p$', ylabel='Variance overhead $R(p)$',
               xlim=(0, .45), ylim=(.8, 130), yscale='log')
        ax.set_xticks([0, .1, .2, .3, .4])
        ax.text(.035, .94, '$z=0$; equal shot counts', transform=ax.transAxes,
                va='top', fontsize=9)
        ax.text(.50, .07, 'Ideal: $R=1$', transform=ax.transAxes, fontsize=9)
        fig.canvas.draw()
        renderer = fig.canvas.get_renderer()
        boxes = [ax.get_tightbbox(renderer)]
        assert all(b.x0 >= 0 and b.y0 >= 0 and b.x1 <= fig.bbox.x1
                   and b.y1 <= fig.bbox.y1 for b in boxes)
        geometry = {'canvas_mm': [85, 76],
                    'axes_mm': [85*.73, 76*.75], 'font_pt': 9,
                    'bounding_box_check': 'passed',
                    'numerical_table_comparison': 'passed (four specified values)',
                    'visual_inspection': 'not established by this script'}
        export(fig, out / 'variance-overhead', dpi=300)
        plt.close(fig)
    (out / 'generation-checks.json').write_text(json.dumps(geometry, indent=2)+'\n',
                                               encoding='utf-8')


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    generate(parser.parse_args().out)
