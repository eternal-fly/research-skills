# Quantum hardware, sensing and learned-workflow evidence routes

Use these routes when the claim concerns an implemented capability or a learned processor applied to quantum data/control. Combine with [information/resource routes](quantum-figures-information.md) and [many-body routes](quantum-figures-manybody.md) when needed. They are original conditional synthesis from the [reread record](../evidence/quantum-figure-review/README.md), not device specifications or a mandatory figure sequence.

## Readout and measurement chains

**Question:** Does the measurement improvement remain at the relevant duration, error definition, throughput and processing cost?

Define the measured states/observable, signal acquisition, labels or reference measurement, and the classifier/estimator. Match the data and operating conditions when comparing algorithms. Show the error versus integration/readout duration or the actual sensitivity tradeoff rather than an isolated best score. When crosstalk or drift is part of the claim, include a control that isolates it, not merely a larger average test set.

Keep prepared-state, state-assignment and measurement-induced errors distinct where they matter. Include training/calibration and inference/latency costs when practical advantage is claimed. Label array size and any lower-SNR acquisition against a higher-SNR labeling procedure.

**Limit:** improved classification on a small measured array does not establish system-scale fault-tolerant readout. A classical reservoir or matched filter applied to qubit signals is a classical processor of quantum-device data, not automatically quantum computational advantage.

Support: [PRApplied_054](../evidence/quantum-figure-review/sources.md#prapplied-054), [PRApplied_060](../evidence/quantum-figure-review/sources.md#prapplied-060), [PRApplied_061](../evidence/quantum-figure-review/sources.md#prapplied-061), [PRResearch_087](../evidence/quantum-figure-review/sources.md#prresearch-087).

## Control, gates and coherent hardware functions

**Question:** Does the observed operation implement the complete claimed quantum function, or only a component/proxy?

Connect device/control geometry to the relevant spectral or dynamical mechanism, then to the gate/process or state metric. Separate analytic prediction, simulation and measured operation. Use population tests and coherence-sensitive evidence when a coherent function is claimed; population routing alone is insufficient. State calibration, bandwidth, drive/duration and leakage conditions that change the comparison.

Use shared-line/crosstalk, detuning or model-parameter controls where they test the mechanism. Do not label a parameter-perturbation band as shot noise. Distinguish ideal model performance from calibration overhead, additional operations and hardware constraints omitted from it.

**Limit:** a component demonstration does not certify a complete memory/router/processor. An isolated or ideal gate metric need not retain its value with spectators, decoherence or omitted transitions; a coherent control metric should not silently become total device fidelity.

Support: [PRApplied_033](../evidence/quantum-figure-review/sources.md#prapplied-033), [PRApplied_053](../evidence/quantum-figure-review/sources.md#prapplied-053), [PRApplied_059](../evidence/quantum-figure-review/sources.md#prapplied-059), [PRX_036](../evidence/quantum-figure-review/sources.md#prx-036). For pulse design itself, also use the control route in the quantum-information guide.

## Photonic interfaces and conditional operations

**Question:** What usable quantum transformation is achieved, and how do loss, heralding and ancillary resources limit it?

Define input modes/states, ancillas, output modes and the actual measurement/herald event. Pair conditional transformation quality with success probability, resource use or rate. Label ideal scattering/model predictions separately from measured device performance. Use spectral/dynamical comparisons to test the specific mechanism, not to decorate an unexplained success curve.

For detectors or interfaces, identify efficiency, bandwidth, noise and operating conditions needed for the claimed capability. An improvement in one may trade against another. A circuit or state diagram is explanatory evidence, not an experimental validation by itself.

**Limit:** an event that cannot be determined from the available herald measurements must not be described as operationally heralded success. Ancilla count, postselection and irreversible loss belong in the same comparison when they affect usefulness.

Support: [PRApplied_015](../evidence/quantum-figure-review/sources.md#prapplied-015), [PRApplied_041](../evidence/quantum-figure-review/sources.md#prapplied-041), [PRApplied_050](../evidence/quantum-figure-review/sources.md#prapplied-050).

## Sensing precision and operational resource accounting

**Question:** Is the sensitivity bound or signal improvement obtainable by the stated preparation and readout, at the relevant resource budget?

Define the encoded parameter, generator, input versus detected resources, observation/preparation time and achieved readout. Plot the measured estimator or accessible signal when claiming operational performance; keep QFI bounds and prospective sensitivity calculations separately labeled. Compare references under the same loss and resource convention. Pair noise-insensitivity tests with the actual response they constrain.

When size scaling is central, show what else changes with size: interaction/generator strength, preparation time, conditioning and detection efficiency. Include success or photon survival probability if the metric is conditional.

**Counterexamples:** detected-photon-based noise suppression is not a complete input-loss-inclusive sensor benchmark; a favorable QFI exponent can be offset by exponential preparation cost. Nonlinear encoding and linear-local encoding have different resource assumptions, so do not use a familiar limit without its model.

Support: [PRApplied_016](../evidence/quantum-figure-review/sources.md#prapplied-016), [PRX_066](../evidence/quantum-figure-review/sources.md#prx-066), [PRResearch_021](../evidence/quantum-figure-review/sources.md#prresearch-021), [PRResearch_057](../evidence/quantum-figure-review/sources.md#prresearch-057).

## Learned quantum workflows and variational optimization

**Question:** Does a learned rule generalize to the claimed quantum task, and is improvement due to the stated information rather than leakage, resampling or a weak baseline?

Identify whether learning occurs in a classical signal processor, a quantum model or a hybrid control/optimization loop. Record independent units of training, adaptation, validation and test: shots from the same system, different systems and later recalibrations are not interchangeable. Show held-out task performance and any transfer across size, device or time that the claim needs; mark retraining explicitly.

Compare classical/control alternatives at matched data, accuracy, resources and tuning effort. If the baseline is a fixed schedule rather than an optimized family, say so. Couple task error/fidelity to a physical diagnostic only when a mechanism claim is actually supported. State shot, seed, system and calibration variability separately.

**Counterexamples:** more low-shot training points can worsen an optimizer's inferred optimum when its noise model gives falsely small uncertainties. A matched-moment noise control can diagnose this; more data is not an automatic validation. A learned classical readout or model-transfer result does not by itself prove a quantum-learning advantage. This corpus does not establish a universal quantum-reservoir figure template.

Support: [PRApplied_060](../evidence/quantum-figure-review/sources.md#prapplied-060), [PRApplied_065](../evidence/quantum-figure-review/sources.md#prapplied-065), [PRResearch_012](../evidence/quantum-figure-review/sources.md#prresearch-012), [PRResearch_058](../evidence/quantum-figure-review/sources.md#prresearch-058), [PRResearch_079](../evidence/quantum-figure-review/sources.md#prresearch-079), [PRResearch_087](../evidence/quantum-figure-review/sources.md#prresearch-087).

## Quantum simulation and optimization benchmarks

**Question:** Is the output task and accuracy comparable, and does a scaling statement survive concrete competing implementations?

Separate algorithmic scaling, measured runtime, compilation/resource estimates and extrapolation. Include optimized relevant classical alternatives when making an advantage claim, including accelerator/device assumptions where they materially change the result. Show accuracy or objective quality alongside runtime/cost, and state input/output overhead and any precomputation excluded.

For learned Hamiltonian/Lindbladian simulation, connect model fit to observable predictions, residuals and error/covariance bounds. A good fit to training observables is not automatically reliable prediction outside them. Small hardware validation establishes the tested regime, not an unmeasured large-scale advantage.

**Limit:** a changed GPU baseline or runtime convention can reverse an apparent advantage; asymptotic improvement and a practical crossover are different claims. Do not label a theorem bound as an observed error bar.

Support: [PRApplied_031](../evidence/quantum-figure-review/sources.md#prapplied-031), [PRApplied_046](../evidence/quantum-figure-review/sources.md#prapplied-046), [PRApplied_074](../evidence/quantum-figure-review/sources.md#prapplied-074), [PRX_049](../evidence/quantum-figure-review/sources.md#prx-049).

## Layout evidence

Actual inspected examples include [PRX_049](../evidence/quantum-figure-review/sources.md#prx-049) p5/Fig2, which uses a full-width linked model-residual/parameter/dissipation/covariance comparison, and [PRX_036](../evidence/quantum-figure-review/sources.md#prx-036) p3/Fig2, which keeps mechanism, population and coherence tests in one column. These observations motivate preserving the comparison while testing single-column readability; they do not imply a hardware platform fixes the number, width or shape of panels.
