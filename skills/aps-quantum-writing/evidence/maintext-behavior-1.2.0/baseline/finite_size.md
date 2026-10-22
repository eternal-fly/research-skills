**Synthetic editorial test**

# Finite-size and time-window dependence of spin imbalance in a disordered Heisenberg chain

## Abstract

A positive late-time imbalance can indicate substantial memory of an initial spin pattern while still evolving with observation time and system size. We examine this distinction in an open disordered spin-1/2 Heisenberg chain by comparing disorder-averaged imbalance over two consecutive time windows for lengths from 12 to 24. The imbalance is larger at disorder strength \(W=6\) than at \(W=3\) throughout the supplied finite-system results. At both strengths, however, every reported mean decreases with increasing length and with the later window. At \(W=6\), the mean over times 80–120 falls from 0.600 to 0.450 between the smallest and largest chains. These comparisons support stronger finite-time retention at \(W=6\), while leaving a nonzero infinite-time thermodynamic plateau undetermined.

## I. MEMORY AND STABILITY OF A LATE-TIME SIGNAL

The relaxation of a spatial spin pattern provides a direct way to examine memory in an interacting disordered chain. Starting from a Néel product state, the staggered magnetization measures how much of the initial alternation remains in the local spin expectations. Exchange couples neighboring spins, while the random longitudinal fields distinguish their local energies. The resulting imbalance is therefore an observable of the dynamics of the prepared pattern, with a normalization that makes its initial value unity.

A positive late-time value alone does not resolve whether that memory has reached a stable level. A signal can remain appreciable over a finite observation interval and still decrease when the interval is moved later or the chain is enlarged. These two comparisons address different aspects of the plateau interpretation: changing the window probes continued evolution, whereas changing the length probes whether the observed level is stable across finite systems. Both are needed to interpret a persistent signal beyond a single trajectory or system size.

Here we ask whether the late imbalance supports a size-stable memory plateau over the measured windows. The evidence consists of converged finite-system window averages at two disorder strengths, four lengths, and two consecutive intervals, each estimated from 32 disorder realizations. Comparing these summaries separates a pronounced disorder dependence of retention from stabilization with time and size. The distinction matters because a stronger retained signal and a stable asymptotic memory are different physical conclusions, even when they concern the same observable.

## II. MODEL AND DISORDER-AVERAGED OBSERVABLE

We consider the open spin-1/2 chain

\[
H=J\sum_{j=1}^{L-1}\left(S_j^xS_{j+1}^x+S_j^yS_{j+1}^y+S_j^zS_{j+1}^z\right)
+\sum_{j=1}^{L}h_jS_j^z,
\tag{1}
\]

where the fields are independently uniform on \([-W,W]\). We set \(\hbar=J=1\), so time is measured in inverse exchange units. The lengths are \(L=12,16,20,24\), and the disorder strengths are \(W=3,6\). The initial state is \(|\psi_0\rangle=|\uparrow\downarrow\uparrow\downarrow\cdots\rangle\). For realization \(r\), evolution under its Hamiltonian \(H_r\) defines

\[
I_r(t)=\frac{2}{L}\sum_{j=1}^{L}(-1)^{j+1}
\langle\psi_0|e^{iH_rt}S_j^ze^{-iH_rt}|\psi_0\rangle.
\tag{2}
\]

The spin eigenvalues \(\pm1/2\) give \(I_r(0)=1\). A positive imbalance thus expresses alignment of the local spin expectations with the initial staggered pattern.

We average over the equal-duration windows \([a_1,b_1]=[40,80]\) and \([a_2,b_2]=[80,120]\), defining

\[
X_r^{(k)}=\frac{1}{40}\int_{a_k}^{b_k}I_r(t)\,dt,
\qquad
\overline X_k=\frac{1}{N}\sum_{r=1}^{N}X_r^{(k)},
\qquad N=32.
\tag{3}
\]

Each \((L,W)\) point uses exactly 32 independent realizations. The two windows at that point use the same realization set; samples at different lengths are drawn independently. The analysis takes the supplied, numerically converged finite-system summaries as input. Each quoted uncertainty is the standard error of the mean (SEM) across the 32 realization means, rather than an integration error or the fluctuation of a trajectory within a window. The Supplement derives this estimator and the uncertainty of differences between windows.

## III. RETENTION AND ITS FINITE-SIZE DRIFT

Table I gives the complete set of supplied means and SEMs. The larger imbalance at \(W=6\) appears at every length in both windows. For example, at \(L=24\) the later-window values are \(0.450\pm0.022\) and \(0.040\pm0.015\) for \(W=6\) and \(W=3\), respectively. This ordering is maintained across the table, establishing a consistent finite-time contrast in the retained staggered signal.

**Table I.** Disorder-averaged imbalance in two time windows for an open Heisenberg chain initialized in the Néel state. Entries are mean \(\pm\) SEM over 32 independent disorder realizations per \((L,W)\). The same realizations contribute to both columns within a row. Time and disorder strength use \(\hbar=J=1\).

| \(W\) | \(L\) | \(\overline X_1\), \(40\le t\le80\) | \(\overline X_2\), \(80\le t\le120\) |
|---:|---:|---:|---:|
| 3 | 12 | 0.180 ± 0.020 | 0.120 ± 0.020 |
| 3 | 16 | 0.150 ± 0.018 | 0.090 ± 0.018 |
| 3 | 20 | 0.120 ± 0.017 | 0.060 ± 0.016 |
| 3 | 24 | 0.100 ± 0.016 | 0.040 ± 0.015 |
| 6 | 12 | 0.620 ± 0.025 | 0.600 ± 0.025 |
| 6 | 16 | 0.580 ± 0.024 | 0.550 ± 0.024 |
| 6 | 20 | 0.540 ± 0.023 | 0.500 ± 0.023 |
| 6 | 24 | 0.500 ± 0.022 | 0.450 ± 0.022 |

The retained level also changes systematically with length. At \(W=3\), increasing \(L\) from 12 to 24 lowers the first-window mean from 0.180 to 0.100 and the second-window mean from 0.120 to 0.040. At \(W=6\), the corresponding changes are 0.620 to 0.500 and 0.600 to 0.450. Every intermediate length continues the downward ordering. The larger values at stronger disorder therefore coexist with a visible dependence on size.

Because the length ensembles are independent, their endpoint differences admit SEM estimates by adding the two endpoint variances. In the later window, \(\overline X_2(12,W)-\overline X_2(24,W)\) is 0.080 with SEM 0.025 at \(W=3\), and 0.150 with SEM 0.033 at \(W=6\). These comparisons quantify the observed size drift without assigning a fitted large-size limit. Four lengths do not determine a unique continuation of the trend.

Moving to the later window lowers the reported mean in every row. At \(W=3\), the difference \(\overline X_1-\overline X_2\) is 0.060 for all four lengths. At \(W=6\), it is 0.020, 0.030, 0.040, and 0.050 as the length increases. These are differences of point estimates. Their sampling uncertainty depends on the covariance between the two window means for the same realization, which is absent from the supplied summaries. Marginal SEMs alone therefore do not provide a paired significance test of the temporal changes. The averages also leave the detailed variation within each window unresolved.

## IV. PHYSICAL INTERPRETATION AND CONCLUSION

The combined size and window comparisons answer the plateau question at the level accessible to these data. Stronger disorder is associated with substantially greater retention of the initial staggered pattern over times 40–120. Nevertheless, the observed means continue to fall when either length or observation time is increased. A common, size-stable late-time level is consequently not established over the measured range.

This conclusion separates the amplitude of finite-time memory from its limiting behavior. These finite summaries leave open continuations toward zero or toward a positive eventual level. Selecting between such continuations requires evidence that constrains the approach to the limits; no extrapolation model is specified by these summaries. In particular, a nonzero infinite-time thermodynamic plateau cannot be inferred from the finite values alone. The uncertainty of the paired temporal differences is a separate, identifiable statistical question that can be resolved by retaining the paired realization means.

For the open chains studied here, the substantive result is stronger finite-time spin-pattern retention at \(W=6\) together with persistent size and window dependence of its measured mean. The imbalance remains a useful quantitative memory observable, but its magnitude and its stability must be assessed independently. The present comparison establishes the former contrast while keeping the latter tied to the measured finite systems.

---

# Supplement: Disorder sampling and uncertainty of window comparisons

## S1. Sample mean and its standard error

At fixed \((L,W)\), let \(X_r^{(k)}\) be the realization-level window average defined in Eq. (3). For a given window, the independent disorder draws make these variables independent and identically distributed. Denote their population mean and variance by \(\mu_k\) and \(\sigma_k^2\). Linearity of expectation and independence give

\[
\mathbb E[\overline X_k]=\mu_k,
\qquad
\operatorname{Var}(\overline X_k)=\frac{\sigma_k^2}{N}.
\tag{S1}
\]

The variance is estimated from the realization means, not from individual time samples. The identity

\[
\sum_r(X_r^{(k)}-\overline X_k)^2
=\sum_r(X_r^{(k)}-\mu_k)^2-N(\overline X_k-\mu_k)^2
\tag{S2}
\]

has expectation \((N-1)\sigma_k^2\). Thus the unbiased sample variance and the usual estimated SEM are

\[
s_k^2=\frac{1}{N-1}\sum_r(X_r^{(k)}-\overline X_k)^2,
\qquad
e_k=\frac{s_k}{\sqrt N}
=\left[\frac{\sum_r(X_r^{(k)}-\overline X_k)^2}{N(N-1)}\right]^{1/2}.
\tag{S3}
\]

Here \(N=32\), giving \(N(N-1)=992\). Although \(s_k^2\) is unbiased for the population variance, taking its square root does not generally produce an unbiased standard-deviation estimator. The table uses the conventional SEM in Eq. (S3). Its meaning is disorder-sampling uncertainty of the estimated ensemble mean. Time points within one realization do not create additional independent disorder samples, and this SEM does not measure numerical integration accuracy.

## S2. Paired changes between windows

For each realization define the decrease \(D_r=X_r^{(1)}-X_r^{(2)}\), whose sample mean is \(\overline D=\overline X_1-\overline X_2\). The sample covariance of the paired window means is

\[
s_{12}=\frac{1}{N-1}\sum_r
(X_r^{(1)}-\overline X_1)(X_r^{(2)}-\overline X_2).
\tag{S4}
\]

Expanding the squared deviation of \(D_r\) gives

\[
s_D^2=s_1^2+s_2^2-2s_{12},
\qquad
e_D^2=\frac{s_D^2}{N}
=e_1^2+e_2^2-\frac{2s_{12}}{N}.
\tag{S5}
\]

Disjoint time windows do not remove this covariance: both are generated by the same random fields and initial state. A realization retaining relatively large imbalance in one window can also retain relatively large imbalance in the other. The covariance, including its sign, must be measured rather than assigned from that possibility.

Writing \(\rho=s_{12}/(s_1s_2)\), the admissible correlation range yields the algebraic bounds

\[
|e_1-e_2|\le e_D\le e_1+e_2.
\tag{S6}
\]

For \(L=24,W=6\), the reported decrease is 0.050, but the two SEMs of 0.022 alone allow \(e_D\) between 0 and 0.044. They therefore do not identify its uncertainty. Adding marginal variances would implicitly set the unknown covariance to zero.

The 32 paired values \((X_r^{(1)},X_r^{(2)})\) at each point would determine Eq. (S4) directly. Equivalently, the sample variance of the 32 differences, or the cross-product sum \(\sum_rX_r^{(1)}X_r^{(2)}\) together with the existing marginal summaries, is sufficient to recover the paired SEM, subject to reporting precision. The paired values also permit inspection of the difference distribution when choosing a confidence-interval or testing procedure. A formal significance test requires that procedure and its assumptions; marginal error bars do not supply them. Raw trajectories would allow the windows themselves to be recomputed, but are unnecessary for Eq. (S5) if the paired means are retained.

## S3. Comparisons across independently sampled lengths

At a fixed disorder strength and window, independent length ensembles have zero sampling covariance. For lengths \(L_a\) and \(L_b\), the estimated SEM of their mean difference is therefore

\[
e_{a-b}=\sqrt{e_a^2+e_b^2}.
\tag{S7}
\]

Using the later-window endpoint entries gives \(\sqrt{0.020^2+0.015^2}=0.025\) at \(W=3\) and \(\sqrt{0.025^2+0.022^2}=0.0333\) at \(W=6\). These sampling uncertainties describe finite-size contrasts. Neither their calculation nor the numerical convergence of each finite-system evolution supplies an extrapolation to an infinite-time thermodynamic memory.
