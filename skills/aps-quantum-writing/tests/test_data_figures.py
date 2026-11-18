"""Palette compatibility and numerical checks for the visual-form gallery."""
import json
from pathlib import Path
import sys
import unittest

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from aps_figure_style import COLORS, data_colormap, data_palette, style
from draw_data_figures import distribution_page, flow_panel, marks_page, scalar_page


class DataFigureTests(unittest.TestCase):
    def test_both_collections_share_lookup_and_keep_the_original_cycle(self):
        catalog = json.loads((ROOT / 'assets/data-palettes.json').read_bytes())
        groups = catalog['collections']
        self.assertEqual(groups['original'], ['aps-cycle', 'cividis', 'RdBu_r'])
        self.assertEqual(len(groups['additional']), 10)
        self.assertEqual(set(groups['original'] + groups['additional']), set(catalog['palettes']))
        self.assertTrue(set(groups['original']).isdisjoint(groups['additional']))
        expected = ('#0072B2', '#D55E00', '#009E73', '#CC79A7', '#222222')
        self.assertEqual(COLORS, expected)
        self.assertEqual(tuple(data_palette()['colors'].values()), expected)
        with style():
            active = mpl.rcParams['axes.prop_cycle'].by_key()['color']
            data_palette('class-identity')['colors'].clear()
            self.assertTrue(data_palette('class-identity')['colors'])
            self.assertEqual(active, list(expected))
            self.assertEqual(mpl.rcParams['axes.prop_cycle'].by_key()['color'], active)
        with self.assertRaises(KeyError):
            data_palette('unknown')
        with self.assertRaises(ValueError):
            data_colormap('aps-cycle')

    def test_catalog_contains_only_named_roles_and_scale_definitions(self):
        catalog = json.loads((ROOT / 'assets/data-palettes.json').read_bytes())
        self.assertEqual(set(catalog), {'scope', 'collections', 'palettes'})
        fields = {'name', 'kind', 'colors', 'encoding', 'stops', 'matplotlib_cmap'}
        for name, entry in catalog['palettes'].items():
            with self.subTest(name=name):
                self.assertTrue(set(entry) <= fields)
                for code in [*entry['colors'].values(), *entry.get('stops', [])]:
                    self.assertRegex(code, r'^#[0-9A-F]{6}$')
                self.assertIn('encoding', entry)

    def test_native_scales_keep_their_entire_lookup_table_and_special_colors(self):
        x = np.ma.array(np.r_[-1, np.linspace(0, 1, 511), 2, 0.5], mask=False)
        x.mask[-1] = True
        for key in ('cividis', 'RdBu_r'):
            original = mpl.colormaps[key]
            local = data_colormap(key)
            np.testing.assert_array_equal(local(x), original(x))
            local.set_bad('red')
            np.testing.assert_array_equal(data_colormap(key)(x), original(x))

    def test_sequential_diverging_and_cyclic_scales(self):
        x = np.linspace(0, 1, 257)

        def lightness(key):
            rgb = data_colormap(key)(x)[:, :3]
            linear = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
            return linear @ [0.2126, 0.7152, 0.0722]

        for key in ('magnitude-blue', 'feature-order'):
            self.assertTrue(np.all(np.diff(lightness(key)) < 0))
        signed = lightness('signed-balance')
        self.assertTrue(np.all(np.diff(signed[:129]) > 0))
        self.assertTrue(np.all(np.diff(signed[128:]) < 0))
        wheel = data_colormap('wrapped-phase')(x)[:, :3]
        self.assertLess(np.linalg.norm(wheel[0] - wheel[-1]), 0.02)
        self.assertGreater(np.linalg.norm(wheel[0] - wheel[128]), 0.5)

    def test_scale_comparison_uses_identical_arrays_and_limits(self):
        fig = scalar_page()
        self.addCleanup(plt.close, fig)
        images = [ax.images[0] for ax in fig.axes if ax.images]
        self.assertEqual(
            [im.get_cmap().name for im in images],
            ['cividis', 'magnitude-blue', 'RdBu_r', 'signed-balance'],
        )
        for a, b in [images[:2], images[2:]]:
            np.testing.assert_array_equal(a.get_array(), b.get_array())
            self.assertEqual(a.get_clim(), b.get_clim())
            np.testing.assert_array_equal(a.get_extent(), b.get_extent())

    def test_marks_share_the_displayed_data(self):
        fig = marks_page()
        self.addCleanup(plt.close, fig)
        points, bars = fig.axes[:2]
        np.testing.assert_allclose(
            points.lines[0].get_xdata(), [rect.get_width() for rect in bars.patches]
        )
        self.assertTrue(all(rect.get_x() == 0 for rect in bars.patches))
        d = distribution_page()
        self.addCleanup(plt.close, d)
        for sample, step in zip(d.axes[0].collections, d.axes[1].lines):
            np.testing.assert_allclose(np.sort(sample.get_offsets()[:, 0]), step.get_xdata()[1:-1])
        self.assertEqual(len(d.axes[2].collections[0].get_offsets()), 700)
        self.assertEqual(d.axes[3].collections[0].get_array().sum(), 700)

    def test_ribbon_width_recovers_the_joint_counts_at_both_ends(self):
        counts = np.array([[4, 2, 7], [1, 6, 2], [3, 1, 1]])
        fig, ax = plt.subplots()
        self.addCleanup(plt.close, fig)
        flow_panel(ax, counts, list(COLORS[:3]))
        for patch, weight in zip(ax.patches, counts.ravel()):
            v = patch.get_path().vertices
            self.assertEqual(v[7, 1] - v[0, 1], weight)
            self.assertEqual(v[4, 1] - v[3, 1], weight)
