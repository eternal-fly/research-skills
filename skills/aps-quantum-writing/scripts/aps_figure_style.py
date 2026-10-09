"""APS-oriented appearance defaults, not journal-mandated themes.
Use at FINAL physical width; do not shrink a completed figure to fit.
Requires Matplotlib. Data selection, fitting and uncertainty remain caller-owned.
"""
from contextlib import contextmanager
from pathlib import Path
import matplotlib as mpl
from cycler import cycler

# Same accessible categorical identity across all journal profiles.
COLORS = ('#0072B2', '#D55E00', '#009E73', '#CC79A7', '#222222')
MARKERS = ('o', 's', '^', 'D', 'v')
LINESTYLES = ('-', '--', '-.', ':', '-')
PROFILES = {
    'prl': {'width_mm': 85, 'height_mm': 105},
    'pra': {'width_mm': 85, 'height_mm': 68},
    'prb': {'width_mm': 178, 'height_mm': 76},
    'prx-quantum': {'width_mm': 178, 'height_mm': 125},
}
# Width 85 mm follows APS single-column guidance. 178 mm is a configurable
# working double-column canvas, NOT a universal APS requirement.
RC = {
    'font.family': 'DejaVu Sans', 'font.size': 9,
    'mathtext.fontset': 'dejavusans', 'text.usetex': False,
    'axes.labelsize': 9, 'axes.titlesize': 9, 'axes.linewidth': .7,
    'axes.prop_cycle': cycler(color=COLORS),
    'axes.grid': False, 'axes.formatter.use_mathtext': True,
    'xtick.labelsize': 9, 'ytick.labelsize': 9,
    'xtick.direction': 'in', 'ytick.direction': 'in',
    'xtick.major.size': 3, 'ytick.major.size': 3,
    'xtick.major.width': .7, 'ytick.major.width': .7,
    'xtick.minor.size': 1.6, 'ytick.minor.size': 1.6,
    'xtick.minor.width': .6, 'ytick.minor.width': .6,
    'lines.linewidth': 1.1, 'lines.markersize': 4,
    'lines.markeredgewidth': .7, 'errorbar.capsize': 2,
    'legend.fontsize': 9, 'legend.frameon': False,
    'legend.handlelength': 1.7, 'legend.borderpad': .2,
    'figure.facecolor': 'white', 'axes.facecolor': 'white',
    'savefig.facecolor': 'white', 'savefig.transparent': False,
    'pdf.fonttype': 42, 'ps.fonttype': 42, 'svg.fonttype': 'none',
    'figure.dpi': 150, 'savefig.dpi': 600,
}

@contextmanager
def style():
    """Temporary rcParams; importing this module does not change global style."""
    with mpl.rc_context(RC):
        yield


def size(journal, width_mm=None, height_mm=None):
    p = PROFILES[journal]
    return ((width_mm if width_mm is not None else p['width_mm']) / 25.4,
            (height_mm if height_mm is not None else p['height_mm']) / 25.4)


def panel(ax, letter):
    """Place panel label inside reserved upper-left whitespace; check overlap."""
    return ax.text(.025, .97, f'({letter})', transform=ax.transAxes,
                   va='top', ha='left', fontsize=9, fontweight='bold')


def export(fig, stem, formats=('pdf', 'png'), dpi=600):
    """Preserve physical canvas. No bbox_inches='tight' (would change width).
    PDF: embedded TrueType text + vector paths; artist rasterization is explicit.
    PNG: entire figure raster. EPS optionally supported for opaque artwork;
    transparency must be resolved deliberately before EPS export.
    """
    stem = Path(stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    for ext in formats:
        fig.savefig(stem.with_suffix('.' + ext), dpi=dpi, bbox_inches=None)
