# Synthetic two-mode mechanism examples

All figures are computed from A = [[-κa/2-iΔ, -ig], [-ig, -κb/2]], with κa=1 and κb=0.08. κ denotes an energy-decay rate or full linewidth; the amplitude-decay rate is κ/2. These are pedagogical calculations, not experiments or an established novelty claim. Couplings, detunings and frequencies are in units of κa.

## response_map.pdf (178 × 69 mm working double-column canvas)
(a) Squared driven response |a(ω)|² at g=0.1 over drive frequency and bare mode-a detuning, for unit drive amplitude in normalized units. The logarithmic color scale has fixed limits 0.01–4; dashed line marks Δ=0. (b) The corresponding Δ=0 spectrum compared with the uncoupled g=0 response, retaining identical bare loss rates. The map establishes parameter dependence; the cut exposes the narrow interference feature. A spectrum alone does not locate stored energy. No incoherent-path or dephasing control is plotted because their definitions/solver outputs were not supplied.

## pole_trajectory.pdf (85 × 82 mm working single-column canvas)
Computed amplitude-generator poles at Δ=0 for 0≤g≤0.6. Vertical axis is amplitude damping, not full linewidth; horizontal axis is pole frequency. Two connected branches approach the exceptional point g=0.23 then separate in frequency at equal damping 0.27. Markers locate g=0, 0.1 and 0.25. At g=0.1 the damping rates are approximately 0.06288 and 0.47712. At g=0.25 both damping rates are 0.27: the weak-coupling slow-pole argument cannot be carried unchanged into this regime.

## dynamics.pdf (178 × 68 mm working double-column canvas)
Free evolution from a(0)=1, b(0)=0 using matrix exponentials. (a) Early-time energies show transfer into b at g=0.1 and compare a with the uncoupled control; the inset enlarges the small transferred population on the same time interval. (b) Total energy on a log scale shows the late-time tail compared with g=0. The total decreases monotonically because d(|a|²+|b|²)/dt = -κa|a|²-κb|b|². The g=0 control transfers no amplitude to b; coupling redistributes excitation without altering the bare damping parameters. Curves are deterministic model solutions, not single-shot stochastic trajectories or ensemble statistics.

## Reproduction and limits
Run python scripts/generate_mechanism_examples.py --out assets/mechanism-examples. Run python -m unittest discover -s tests. NumPy, SciPy and Matplotlib are required. PDF/PNG exports retain canvas dimensions; these widths are configurable working presets, not journal-specific aspect-ratio mandates. Do not infer error bars, noise resilience, nonlinear protection, phase transitions or a thermodynamic limit from this model. The footprint function explicitly chooses single/double width and height, independently of journal. Legacy aps_figure_style.size remains unchanged for compatibility.
