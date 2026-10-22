# Quantum information, computation and certification evidence routes

Select routes by the actual claim and use the [fixed planning record](figure-planning-record.md). Each route can require a curve, diagram, table, exact expression or no data figure. The [source review](../evidence/quantum-figure-review/README.md) supports conditional editorial choices, not universal APS figure templates or verified algorithmic correctness.

## Logical protection, recovery and decoding

**Question:** What logical benefit is established, at what physical/operational cost, and which intervention causes it?

Define code, rounds, extraction circuit, noise assumptions and the denominator of logical error: per round, per experiment and per accepted shot differ. Compare at matched target error or resource when appropriate. If selecting outcomes, expose acceptance, expected attempts or spacetime cost beside conditional error. A favorable threshold curve alone may hide an unfavorable operating point.

Test the intervention implicated by the claim: fixed code/changed recovery versus joint optimization; leakage reduction versus richer readout; changed decoder versus changed noise information. Keep inaccessible, high-weight or nonlocal operations distinct from hardware-feasible ones. Latency claims need the relevant tail/deadline diagnostic, not only average runtime. Separate sampled probabilities, zero-event upper bounds, fits and threshold extrapolations; record sample counts and uncertainty conventions.

**Limit:** optimized logical performance under unconstrained recovery does not establish an implementable device improvement. Better conditional error without its yield/cost is not a complete operational advantage.

Support: [PRA_048](../evidence/quantum-figure-review/sources.md#pra-048), [PRXQuantum_011](../evidence/quantum-figure-review/sources.md#prxquantum-011), [PRXQuantum_057](../evidence/quantum-figure-review/sources.md#prxquantum-057), [PRXQuantum_064](../evidence/quantum-figure-review/sources.md#prxquantum-064), [PRXQuantum_068](../evidence/quantum-figure-review/sources.md#prxquantum-068).

## Heralded or postselected protocols

**Question:** Does improved conditional quality remain useful after success probability, input dependence and model knowledge are included?

State the selected event and ensemble. Pair conditioned fidelity/distance with acceptance probability, repeated-attempt cost or useful output rate. If input selection changes the ensemble, distinguish input-resolved variation from estimator error bars. Compare deterministic/unfiltered references and resource-matched alternatives where scientifically relevant.

Label achievable performance versus upper/lower bounds. For protocols that rely on calibration or assumed parameters, show actual-versus-assumed mismatch when robustness is claimed. A perfect-knowledge line is not a robustness test. Separate a herald observable from a success event that is not experimentally heraldable.

**Limit:** unit conditional fidelity can coexist with small throughput; an improved average need not imply input-uniform performance. Avoid hiding these distinctions by plotting only the best input or retained subset.

Support: [PRA_012](../evidence/quantum-figure-review/sources.md#pra-012), [PRA_028](../evidence/quantum-figure-review/sources.md#pra-028), [PRA_038](../evidence/quantum-figure-review/sources.md#pra-038), [PRA_099](../evidence/quantum-figure-review/sources.md#pra-099), [PRXQuantum_028](../evidence/quantum-figure-review/sources.md#prxquantum-028).

## Algorithms, compilation and resource bounds

**Question:** Which task and access model improve, and does the resource comparison include the cost relevant to that claim?

Define error norm/target and task-dependent axes such as size, evolution time, overlap or condition number. Select relevant tradeoffs among gate count, ancillas, depth, copies, repetitions, state preparation, classical optimization and output extraction; do not demand every resource when the theorem concerns a narrower model.

Separate a proved bound from compiled values, empirical fits and extrapolations. A proof diagram or assumptions-and-bounds table can be more informative than a synthetic scaling plot. When numerical validation is appropriate, compare the actual observable/error to a reference, include residuals where overlapping curves hide the decisive error, and mark failures or unavailable exact benchmarks.

**Limit:** small hardware demonstrations and special benchmark instances do not automatically show end-to-end advantage. Classical baselines must match the output task and accuracy. Lower subroutine cost can trade against width, repetitions or input/output cost rather than reduce runtime.

Support: [PRXQuantum_013](../evidence/quantum-figure-review/sources.md#prxquantum-013), [PRXQuantum_026](../evidence/quantum-figure-review/sources.md#prxquantum-026), [PRXQuantum_038](../evidence/quantum-figure-review/sources.md#prxquantum-038), [PRXQuantum_085](../evidence/quantum-figure-review/sources.md#prxquantum-085), [PRA_017](../evidence/quantum-figure-review/sources.md#pra-017), [PRA_081](../evidence/quantum-figure-review/sources.md#pra-081).

## Certification, witnesses and quantum resources

**Question:** Does the reported metric certify the claimed property, or respond to a confounder?

State the property, threshold, assumptions and direction of each bound. A sufficient witness, a necessary condition and a complete characterization within a restricted family are different. Include a negative control or counterexample that tests the relevant ambiguity when it changes the inference: local mixedness versus entanglement, stabilizer expectation versus fidelity, or privacy versus simply erasing useful information.

Connect operational claims to preparation fidelity, shot/confidence budget and measurement completeness where needed. Separate state-set schematics, finite numerical examples and rigorous characterizations. A finite parameter search cannot establish absence outside its domain.

**Limit:** resource proxies cannot silently substitute for the resource itself. Distinguish measured quantities from reconstructed or bounded ones, and preserve finite-sample guarantees rather than drawing uncertainty from curve appearance.

Support: [PRA_005](../evidence/quantum-figure-review/sources.md#pra-005), [PRA_050](../evidence/quantum-figure-review/sources.md#pra-050), [PRA_079](../evidence/quantum-figure-review/sources.md#pra-079), [PRXQuantum_035](../evidence/quantum-figure-review/sources.md#prxquantum-035), [PRXQuantum_065](../evidence/quantum-figure-review/sources.md#prxquantum-065).

## Noise, channels and identifiability

**Question:** Which model components can be identified from the measurement, and does the inferred model make valid operational predictions?

Define observables, control restrictions and whether the target is a unique parameter vector, an equivalence class or a gauge-consistent prediction. Compare known truth when available, but validate on a diagnostic sensitive to ambiguities rather than merely replotting the fitted training data.

For drifting noise, expose the window/bandwidth and bias/variance tradeoff. For spectral reconstruction, test unresolved features between grid points when they matter. Distinguish shot variation, independent trajectories, training seeds, drift realizations and fitted-parameter uncertainty. State the resolution or model assumptions under which a spectral feature can be resolved.

**Limit:** an unidentifiable parameter is not uniquely learned because one fit converged. Agreement at sampled frequencies alone need not validate the spectrum between them.

Support: [PRXQuantum_016](../evidence/quantum-figure-review/sources.md#prxquantum-016), [PRXQuantum_027](../evidence/quantum-figure-review/sources.md#prxquantum-027), [PRXQuantum_046](../evidence/quantum-figure-review/sources.md#prxquantum-046), [PRA_065](../evidence/quantum-figure-review/sources.md#pra-065).

## Quantum control and gate design

**Question:** Does the waveform/design explain the relevant error reduction under matched constraints?

Connect control waveform to the transition/spectrum, accumulated phase or leakage channel that supports the mechanism, and then to the operational gate metric. Sweep the resource or vulnerability central to the claim: time, detuning, strength, leakage or calibration mismatch. Distinguish analytic design, numerical adjustment and experimental calibration.

Compare controls under stated bandwidth/amplitude/duration and model constraints. Separate coherent/unitary control error from open-system total error. Account for the actual target distribution if averaging random gates. Use the [device route](quantum-figures-devices.md) when implementation and measured hardware performance are central.

**Limit:** a simulated error frontier omitting distortions, heating or padding is not measured device performance; a selected pulse trace does not establish robustness across the relevant target family.

Support: [PRXQuantum_007](../evidence/quantum-figure-review/sources.md#prxquantum-007), [PRXQuantum_032](../evidence/quantum-figure-review/sources.md#prxquantum-032), [PRA_064](../evidence/quantum-figure-review/sources.md#pra-064).

## Sensing and communication resources

**Question:** Does the useful task improve after preparation, loss, measurement and throughput conditions are made explicit?

For sensing, define the estimated parameter/combination and the conserved resource. Pair sensitivity with privacy or robustness only when both remain nontrivial; erasing all useful information can make a privacy score look good. Distinguish a quantum Fisher-information bound from achieved estimator performance. Show the preparation/measurement threshold when the scaling claim depends on it.

For communication, compare rate at matched distance, hardware, loss and required output quality. Mark configurations that fail fidelity/security conditions. Distinguish finite-key from asymptotic results and match security parameters. Optimization runtime is separate from physical communication throughput.

**Limit:** shot-based, detected-particle-based and input-resource-based comparisons are not interchangeable. A bound, conditional metric or optimized model curve should retain its operational assumptions.

Support: [PRXQuantum_004](../evidence/quantum-figure-review/sources.md#prxquantum-004), [PRA_011](../evidence/quantum-figure-review/sources.md#pra-011), [PRA_068](../evidence/quantum-figure-review/sources.md#pra-068), [PRXQuantum_020](../evidence/quantum-figure-review/sources.md#prxquantum-020), [PRXQuantum_035](../evidence/quantum-figure-review/sources.md#prxquantum-035), [PRXQuantum_090](../evidence/quantum-figure-review/sources.md#prxquantum-090).

## Layout observations

Pixel-inspected published examples include [PRXQuantum_011](../evidence/quantum-figure-review/sources.md#prxquantum-011) p5/Fig4 (device/circuit and quantitative subpanels within one column), [PRXQuantum_035](../evidence/quantum-figure-review/sources.md#prxquantum-035) p11/Fig6 (four quantitative panels in one column), [PRXQuantum_057](../evidence/quantum-figure-review/sources.md#prxquantum-057) p7/Fig4 (double-column quality/cost frontier plus feasibility maps), and [PRXQuantum_026](../evidence/quantum-figure-review/sources.md#prxquantum-026) p13/Fig4 (double-column gate/ancilla comparisons). These examples refute a width rule based only on panel count. Keep single column if the physical comparison and final-size text remain readable; otherwise record the reason for widening. Do not infer width from captions or from a role label.
