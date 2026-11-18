"""Draw an original two-spin schematic and calculate its illustrative readout."""
import argparse
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path as VectorPath
import numpy as np

from aps_figure_style import export, schematic_palette, style


def readout_trace(theta, phi, p, periods):
    """Stroboscopic <Z_1> after unitary evolution followed by joint reset."""
    eye = np.eye(2)
    x = np.array([[0, 1], [1, 0]])
    z = np.diag([1, -1])
    rotation = np.cos(theta / 2) * eye - 1j * np.sin(theta / 2) * x
    coupling = np.diag(np.exp(-0.5j * phi * np.diag(np.kron(z, z))))
    cycle = coupling @ np.kron(rotation, rotation)
    ground = np.diag([1., 0., 0., 0.])
    observable = np.kron(z, eye)
    state = ground.copy()
    values = [1.]
    for _ in range(periods):
        state = (1 - p) * (cycle @ state @ cycle.conj().T) + p * ground
        values.append(np.trace(observable @ state).real)
    return np.array(values)


def draw(output):
    colors = schematic_palette('floquet')
    ink = colors['ink']
    width, height = 85, 63
    with style(), matplotlib.rc_context({'svg.hashsalt': 'aps-two-spin-period'}):
        fig = plt.figure(figsize=(width / 25.4, height / 25.4))
        ax = fig.add_axes([0, 0, 1, 1], xlim=(0, width), ylim=(0, height), aspect='equal')
        ax.set_axis_off()

        def label(x, y, s, size=9, align='left', **kwargs):
            return ax.text(x, y, s, fontsize=size, ha=align, va='center', color=ink, **kwargs)

        def box(x, y, w, h, fill, edge, radius=0.8, lw=0.7, zorder=2.5):
            ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f'round,pad=0,rounding_size={radius}',
                                        facecolor=fill, edgecolor=edge, linewidth=lw, zorder=zorder))

        def line(xs, ys, **kwargs):
            ax.plot(xs, ys, solid_capstyle='round', **kwargs)

        # A single field groups a period. The two spin wires supply the geometry.
        box(10.4, 38.5, 41.1, 22.8, colors['field'], colors['boundary'], radius=2.1, lw=.65, zorder=0)
        label(13.0, 58.1, 'Floquet period', 9.2, weight='semibold')
        for y, index in [(50.5, 1), (42.1, 2)]:
            label(1.7, y, rf'$q_{index}$', 11.3)
            line([7.7, 70.5 if index == 1 else 67.0], [y, y], color=ink, lw=.8)
            box(15.4, y - 2.85, 14.3, 5.7, colors['gate'], ink)
            label(22.55, y, r'$R_x(\theta)$', 10.0, 'center')

        # A symmetric Ising gate acts on both spins. The warm point marks the
        # interaction on the link and has no control/target interpretation.
        for y in (42.1, 50.5):
            ax.add_patch(Circle((38.2, y), .88, facecolor=ink, edgecolor=ink, lw=.5, zorder=3))
        line([38.2, 38.2], [42.1, 50.5], color=ink, lw=1.1)
        ax.add_patch(Circle((38.2, 46.3), 1.18, facecolor=colors['accent'], edgecolor=ink, lw=.6, zorder=3))
        label(40.3, 46.3, r'$ZZ$', 9.5)

        box(55.2, 39.5, 9.2, 13.8, colors['reset'], colors['loop'], radius=1.5, lw=.9)
        label(59.8, 56.8, 'Reset', 8.4, 'center')
        label(59.8, 46.3, r'$\mathcal{R}_p$', 11.4, 'center')
        # The return attaches to the channel and the full period, not a meter.
        route = VectorPath([(59.8, 39.5), (59.8, 35.6), (57.8, 34.4), (54.8, 34.4),
                            (14.6, 34.4), (11.3, 34.4), (11.3, 36.3), (11.3, 38.4)],
                           [VectorPath.MOVETO, VectorPath.CURVE4, VectorPath.CURVE4, VectorPath.CURVE4,
                            VectorPath.LINETO, VectorPath.CURVE4, VectorPath.CURVE4, VectorPath.CURVE4])
        ax.add_patch(FancyArrowPatch(path=route, arrowstyle='-|>', mutation_scale=6.8,
                                     color=colors['loop'], lw=.95, linestyle=(0, (3, 1.8))))
        label(33.5, 34.5, 'next period', 8.2, 'center', bbox=dict(facecolor='white', edgecolor='none', pad=.6))

        box(69.4, 46.3, 12.9, 8.4, colors['measurement'], ink, radius=1.3)
        ax.add_patch(Arc((73.1,49.7),4.4,4.2,theta1=15,theta2=165,color=ink,lw=.85,zorder=3))
        line([73.1,74.4],[49.6,51.9],color=ink,lw=.85,zorder=3)
        label(76.2, 50.5, r'$Z_1$', 10.4)

        # A compact calculated data inset makes the measured observable explicit.
        left, bottom, plot_w, plot_h = 40.0, 9.0, 40.1, 19.7
        trace = fig.add_axes([left / width, bottom / height, plot_w / width, plot_h / height])
        n = np.arange(9)
        for p, c, ls, marker, face in [(0., ink, '--', 'o', 'white'), (.18, colors['loop'], '-', 's', colors['reset'])]:
            values = readout_trace(.74*np.pi, .36*np.pi, p, 8)
            trace.plot(n, values, color=c, ls=ls, lw=.8, marker=marker, markersize=3.1,
                       markerfacecolor=face, markeredgecolor=c, markeredgewidth=.7, clip_on=False,
                       zorder=4 if p==0 else 3)
        trace.set(xlim=(-.05,8.05), ylim=(-1.05,1.08), xticks=[0,4,8], yticks=[-1,0,1])
        trace.tick_params(labelsize=8.0, colors=ink, length=2.3, pad=2)
        trace.spines[['top','right']].set_visible(False)
        for side in ('left','bottom'):
            trace.spines[side].set_color(ink)
        trace.set_xlabel('Period', fontsize=8.5, color=ink, labelpad=0)
        label(2.0, 26.5, 'Model readout', 9.1, weight='semibold')
        label(2.0, 20.7, r'$\langle Z_1\rangle$', 12)
        for y, text, c, ls, marker, fill in [(13.4, r'$p=0$', ink, '--', 'o', 'white'),
                                             (7.7, r'$p=0.18$', colors['loop'], '-', 's', colors['reset'])]:
            line([2.3, 9.2], [y,y], color=c, ls=ls, lw=.9)
            ax.plot(5.75,y,marker=marker,ms=3.7,mec=c,mfc=fill,mew=.7)
            label(11.0,y,text,8.8)
        export(fig, Path(output) / 'floquet-period', formats=('pdf','svg','png'), dpi=360)
        plt.close(fig)


if __name__ == '__main__':
    plt.switch_backend('Agg')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', required=True, type=Path)
    draw(parser.parse_args().out)
