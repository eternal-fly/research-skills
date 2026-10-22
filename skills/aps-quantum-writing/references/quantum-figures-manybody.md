# Quantum simulation and many-body evidence routes

These are conditional editorial routes from the [fresh review](../evidence/quantum-figure-review/README.md), not a mandatory numbered figure set. Begin with the physical discrimination in the [planning record](figure-planning-record.md). The support entries below identify source-specific observations and counterexamples; the generalization is editorial synthesis, not an APS requirement.

## Quantum simulation and state preparation

**Question:** Does the implemented dynamics/state realize the target physics, rather than merely improve a convenient proxy?

Connect model-to-platform mapping and prepared sector to an accessible exact or controlled benchmark, then to the physically decisive observable. If extracting a rate, peak or Fourier feature is essential, keep a raw trace beside the derived quantity. Distinguish exact numerics, an effective model, fit and guide to the eye. Energy agreement alone need not establish state fidelity or correct correlations.

Choose controls for the claimed source of improvement: matched duration/resources, schedule/path equivalence, competing-state overlap, conservation/gauge checks, noise-free versus noisy dynamics, or convergence against step size and truncation. Physical size, bond dimension, local Hilbert cutoff and sampling count are separate variables. Report postselection cost when used.

**Limits:** a short-time dilute process, a mesoscopic state and a thermodynamic phase answer different questions. An ideal adiabatic improvement can lose on hardware at long duration; an intentionally prepared excited state should not be labeled a ground state. Do not require all listed observables or controls when a narrower claim is sufficient.

Support: [PRL_003](../evidence/quantum-figure-review/sources.md#prl-003), [PRL_016](../evidence/quantum-figure-review/sources.md#prl-016), [PRL_059](../evidence/quantum-figure-review/sources.md#prl-059), [PRB_032](../evidence/quantum-figure-review/sources.md#prb-032), [PRB_069](../evidence/quantum-figure-review/sources.md#prb-069), [PRB_089](../evidence/quantum-figure-review/sources.md#prb-089).

## Phase identification and universality

**Question:** Does the apparent change survive the relevant limit, and which competing order or transition class is excluded?

Define geometry, symmetry, control parameters and diagnostics before plotting a phase map. Keep raw multi-size curves or representative cuts visible alongside crossings, extrapolation or collapse. Choose observables that distinguish the candidate phases: order parameters, correlations, Binder ratios, gaps or structure factors as scientifically appropriate. Label boundaries as analytic, measured, fitted or unresolved.

Separate total length, subsystem length, temperature, observation time, bond dimension and numerical resolution. Test fit window, minimum-size cutoff, correction terms and alternative ansatz where the inferred conclusion depends on them. Sampling error is not finite-size uncertainty. BKT behavior must not be forced into ordinary power-law collapse.

**Counterexamples:** a finite-size colored region can shrink away at fixed parameters; a good collapse can coexist with another length scale; some monitored/open transitions need not close the spectral gap. Neither a peak nor a single extrapolated intercept is an automatic thermodynamic certificate.

Support: [PRL_001](../evidence/quantum-figure-review/sources.md#prl-001), [PRL_074](../evidence/quantum-figure-review/sources.md#prl-074), [PRL_098](../evidence/quantum-figure-review/sources.md#prl-098), [PRB_015](../evidence/quantum-figure-review/sources.md#prb-015), [PRB_022](../evidence/quantum-figure-review/sources.md#prb-022), [PRB_045](../evidence/quantum-figure-review/sources.md#prb-045), [PRB_059](../evidence/quantum-figure-review/sources.md#prb-059), [PRB_076](../evidence/quantum-figure-review/sources.md#prb-076).

## Monitored dynamics and mixed-state correlations

**Question:** Which ensemble, measurement conditioning and weighting produce the reported quantum correlations or transition?

Record the measurement basis/efficiency, trajectory ensemble, Born-rule versus forced weighting, normalization and entropy order. Compare with the unmonitored or otherwise mechanism-relevant reference. Pair an entanglement/correlation diagnostic with size/time or purification evidence only when they address the same claim.

The average of a trajectory-connected correlator is not generally the connected correlator of the averaged density matrix. Distinguish trajectory variation, disorder/circuit variation, quantum variance and estimator standard error. Include success probability and its size dependence when postselection affects operational accessibility.

**Limits:** subsystem entropy in a mixed state is not automatically an entanglement witness; use a justified mixed-state measure or explicit witness. A finite logarithmic interval need not be asymptotic, and improving an exponential success exponent does not eliminate exponential cost.

Support: [PRL_014](../evidence/quantum-figure-review/sources.md#prl-014), [PRL_023](../evidence/quantum-figure-review/sources.md#prl-023), [PRL_036](../evidence/quantum-figure-review/sources.md#prl-036), [PRB_060](../evidence/quantum-figure-review/sources.md#prb-060), [PRB_061](../evidence/quantum-figure-review/sources.md#prb-061), [PRB_086](../evidence/quantum-figure-review/sources.md#prb-086), [PRB_100](../evidence/quantum-figure-review/sources.md#prb-100).

## Topology, edge modes and finite-scale quantum liquids

**Question:** Is the signal a bulk topological property, a boundary/symmetry effect or finite-scale topological-looking correlation?

Define physical boundaries, entanglement cuts, symmetry/parity sectors and the actual invariant or operational diagnostic. Combine it with spectra, spatial localization, response or loop/string observables only where the inference requires them. For a prepared spin-liquid-like region, identify subsystem and excitation length scales. For braiding, connect the protocol to its measured fusion/loop signature and appropriate no-braid reference.

Check finite-size splitting, sector averaging, microscopic-versus-effective descriptions, cutoff convergence and conditioning. Compare with a plausible competing state; neither low energy nor one near-quantized entropy value alone certifies the complete target.

**Counterexamples:** a parity crossing need not be a protected Majorana operating point; zero energy is not a localization/protection certificate; degeneracy averaging can cancel a nonlocal diagnostic. Do not transfer invariants or witnesses between pure/mixed and Hermitian/non-Hermitian settings without checking their definitions.

Support: [PRL_059](../evidence/quantum-figure-review/sources.md#prl-059), [PRL_063](../evidence/quantum-figure-review/sources.md#prl-063), [PRL_069](../evidence/quantum-figure-review/sources.md#prl-069), [PRB_019](../evidence/quantum-figure-review/sources.md#prb-019), [PRB_035](../evidence/quantum-figure-review/sources.md#prb-035), [PRB_054](../evidence/quantum-figure-review/sources.md#prb-054), [PRB_073](../evidence/quantum-figure-review/sources.md#prb-073), [PRB_098](../evidence/quantum-figure-review/sources.md#prb-098).

## Open dynamics, transport and relaxation

**Question:** Does the evidence distinguish memory, transport, dissipation or a selected relaxation mechanism from its alternatives?

Define generator/baths, boundaries, preparation, current direction and the distance or observable used. Show raw dynamics or physical response with a mechanism-sensitive comparison: channel change, reciprocal/Markovian limit, initial-state change or boundary-condition control, as appropriate. Use spectral/transmission or mode information only when it tests the asserted explanation.

For a relaxation-crossing claim, expose the initial ordering, common dynamics and relevant final state. Separate finite-time proxy, steady-state result, bound and fit. Distinguish physical linewidth from windowing/broadening, statistical intervals from numerical/model error, and transient entanglement from steady-state quantum correlations.

**Counterexamples:** arbitrary observables can miss slow modes; an unobserved crossing may lie beyond the time window. Removing the slowest exponential mode is not a universal explanation of accelerated relaxation: algebraic/hydrodynamic and boundary-sensitive regimes require different diagnostics.

Support: [PRL_077](../evidence/quantum-figure-review/sources.md#prl-077), [PRL_085](../evidence/quantum-figure-review/sources.md#prl-085), [PRL_089](../evidence/quantum-figure-review/sources.md#prl-089), [PRB_029](../evidence/quantum-figure-review/sources.md#prb-029), [PRB_043](../evidence/quantum-figure-review/sources.md#prb-043), [PRB_057](../evidence/quantum-figure-review/sources.md#prb-057), [PRB_068](../evidence/quantum-figure-review/sources.md#prb-068), [PRB_079](../evidence/quantum-figure-review/sources.md#prb-079), [PRB_081](../evidence/quantum-figure-review/sources.md#prb-081).

## Floquet dynamics, temporal order and scars

**Question:** Is the oscillation robust temporal order, finite-time freezing, a few-level recurrence or initial-state projection?

Define drive, sampling/stroboscopic convention, initial-state class and observation window. Pair time traces with the frequency or spectral-weight evidence needed to distinguish these explanations. Test parameter locking, drive perturbation, initial-state contrast and size/lifetime dependence when the claim invokes robustness or order. Resolve symmetries before level-statistics comparisons.

Distinguish quasienergy pairing, eigenstate structure, spectral overlap, local thermalization, return fidelity and instantaneous-ground-state overlap. A sharp Fourier peak or global revival alone does not certify a time crystal, scar mechanism or useful entanglement. Keep early-time and late-time error-scaling regimes distinct.

Support: [PRL_009](../evidence/quantum-figure-review/sources.md#prl-009), [PRL_017](../evidence/quantum-figure-review/sources.md#prl-017), [PRL_030](../evidence/quantum-figure-review/sources.md#prl-030), [PRL_055](../evidence/quantum-figure-review/sources.md#prl-055), [PRB_013](../evidence/quantum-figure-review/sources.md#prb-013), [PRB_025](../evidence/quantum-figure-review/sources.md#prb-025), [PRB_062](../evidence/quantum-figure-review/sources.md#prb-062), [PRB_083](../evidence/quantum-figure-review/sources.md#prb-083).

## Scrambling and disordered propagation

**Question:** Does an averaged front describe typical dynamics, or conceal heterogeneous realizations and threshold-dependent behavior?

Define the OTOC/commutator, geometry and measurement protocol. A spacetime map with meaningful contours can be paired with distance/time cuts; use raw realization distributions or representative trajectories when averaging hides the distinction. Benchmark time reversal or the measurement protocol separately from the underlying dynamics.

Vary relevant thresholds, fit intervals, boundaries, interaction range and system size. Separate disorder spread from initial-state sampling error. Mask uncomputed/unreliable map cells distinctly from a physical zero. A fitted propagation exponent that changes with threshold or disorder must retain that scope.

Support: [PRB_014](../evidence/quantum-figure-review/sources.md#prb-014), [PRB_030](../evidence/quantum-figure-review/sources.md#prb-030).

## Collective charging and system-size advantage

**Question:** Is the apparent size advantage obtained at matched physical resources and within the claimed asymptotic regime?

Define stored energy, work, average/peak power, target time, battery/charger sizes and normalizations. Pair the claimed advantage with the reference protocol, finite-size range and any parameters that vary simultaneously with size. Use mode occupation or an effective-interaction diagnostic only if actually evaluated and needed for the explanation.

Coupling, range, drive frequency, charger size and initial-state preparation can change the comparison. Separate measured/computed values, theoretical bounds and fitted exponent. A favorable finite-window fit does not itself establish thermodynamic superextensivity.

Support: [PRB_080](../evidence/quantum-figure-review/sources.md#prb-080), [PRB_096](../evidence/quantum-figure-review/sources.md#prb-096), [PRB_097](../evidence/quantum-figure-review/sources.md#prb-097).

## Layout observations, not prescriptions

Pixel-inspected source pages include [PRL_003](../evidence/quantum-figure-review/sources.md#prl-003) p4/Fig2 (full-width unequal-area map/trace comparison), [PRL_001](../evidence/quantum-figure-review/sources.md#prl-001) p4/Figs3–4 (compact single-column comparisons), [PRL_077](../evidence/quantum-figure-review/sources.md#prl-077) p3/Fig1 (seven panels within a single column), [PRB_014](../evidence/quantum-figure-review/sources.md#prb-014) p3/Figs1–2 (maps plus wider time cuts), [PRB_073](../evidence/quantum-figure-review/sources.md#prb-073) p9/Fig3 (full-width paired map-and-cut units), and [PRB_079](../evidence/quantum-figure-review/sources.md#prb-079) p5/Fig5 (four diagnostics in one column). Publication is not a guarantee of optimal readability. These cases support testing comparison geometry rather than choosing width by panel count; they establish neither journal-wide frequencies nor a requirement to imitate the layout.
