from pathlib import Path
import json
import re
import sys
import unittest

import matplotlib as mpl
import numpy as np
from scipy.linalg import expm


SKILL = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL / 'scripts'))
from aps_figure_style import schematic_palette
from draw_floquet_example import readout_trace


class SchematicExampleTests(unittest.TestCase):
    def test_role_palettes_are_independent_of_the_data_cycle(self):
        catalog = json.loads((SKILL / 'assets/schematic-palettes.json').read_text(encoding='utf-8'))
        cycle = mpl.rcParams['axes.prop_cycle']
        names = {study['key'] for study in catalog['studies']}
        self.assertEqual(len(names), 10)
        for name in names | {'floquet'}:
            with self.subTest(name=name):
                roles = schematic_palette(name)
                self.assertTrue(roles)
                self.assertTrue(all(re.fullmatch(r'#[0-9A-Fa-f]{6}', c) for c in roles.values()))
                roles.clear()
                self.assertTrue(schematic_palette(name))
        with self.assertRaises(KeyError):
            schematic_palette('unknown scheme')
        self.assertEqual(mpl.rcParams['axes.prop_cycle'], cycle)

    def test_stroboscopic_readout_by_conditioning_on_the_last_reset(self):
        theta, phi, periods = .74 * np.pi, .36 * np.pi, 8
        x = np.array([[0, 1], [1, 0]])
        z = np.diag([1, -1])
        identity = np.eye(2)
        rotation = expm(-.5j * theta * (np.kron(x, identity) + np.kron(identity, x)))
        cycle = expm(-.5j * phi * np.kron(z, z)) @ rotation
        state = np.array([1., 0., 0., 0.])
        observable = np.kron(z, identity)
        coherent = []
        for _ in range(periods + 1):
            coherent.append(np.vdot(state, observable @ state).real)
            state = cycle @ state
        for p in (0., .18, 1.):
            with self.subTest(reset_probability=p):
                expected = [(1 - p)**n * coherent[n]
                            + p * sum((1 - p)**k * coherent[k] for k in range(n))
                            for n in range(periods + 1)]
                np.testing.assert_allclose(readout_trace(theta, phi, p, periods), expected,
                                           rtol=0, atol=1e-13)
