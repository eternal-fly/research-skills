**Synthetic editorial test**

# Finite-size and time-window dependence of memory in a disordered spin chain

## Abstract

Late-time spin imbalance can reveal retention of an initial spatial pattern, but its magnitude alone does not establish a stable memory plateau. We examine a disordered spin-1/2 Heisenberg chain through two consecutive time windows and four lengths, using 32 disorder realizations at each parameter point. The disorder-averaged imbalance is larger at disorder strength $W=6$ than at $W=3$ throughout the data. At both strengths, however, its central values decrease with length and in the later window. For $W=6$, the mean over times 80–120 falls from 0.600 at length 12 to 0.450 at length 24. These comparisons establish stronger finite-time retention at $W=6$, while the observed size drift leaves a nonzero thermodynamic memory plateau unresolved.

## I. MEMORY AS A DYNAMICAL OBSERVABLE

A staggered spin pattern provides a direct way to ask how much information about an initial state survives interacting dynamics. For a Néel state, neighboring sites begin with opposite magnetization, and the imbalance measures their remaining alignment with that pattern. Its persistence at late times is physically informative even when the eventual fate of the pattern remains uncertain. The distinction is between retaining a substantial fraction of the initial magnetization over an accessible interval and approaching a value that remains stable as both the observation time and system size increase.

That distinction requires two comparisons. Moving the observation window tests whether the measured memory changes at fixed size; increasing the chain length tests whether its magnitude is specific to a small system. A large value in one window addresses neither dependence by itself. Moreover, averaging over time and averaging over disorder have different roles. The first defines the dynamical quantity being measured, whereas the second estimates its mean across field configurations. The uncertainty of a comparison between windows depends on how those configurations are reused.

Here the two comparisons are combined for open chains of lengths $L=12,16,20,24$, at disorder strengths $W=3$ and $6$. The numerical input consists of means over the intervals 40–80 and 80–120, with disorder-sampling errors. These data resolve a consistent ordering between the two disorder strengths and a downward size trend. They therefore allow a substantive assessment of finite-time memory without assigning a limiting value from an assumed extrapolation law.

## II. MODEL AND DISORDER AVERAGING

The Hamiltonian is

\[
H_r=J\sum_{j=1}^{L-1}\left(S_j^xS_{j+1}^x+S_j^yS_{j+1}^y+S_j^zS_{j+1}^z\right)
+\sum_{j=1}^{L}h_{j,r}S_j^z,
\tag{1}
\]

where $S_j^\alpha=\sigma_j^\alpha/2$ are spin-1/2 operators and the fields are independently uniform on $[-W,W]$. Open boundaries are implemented by the $L-1$ exchange bonds. We set $\hbar=J=1$, so time is measured in inverse exchange units. Each realization starts in $|N\rangle=|\uparrow\downarrow\uparrow\downarrow\cdots\rangle$ and evolves as $|\psi_r(t)\rangle=e^{-iH_rt}|N\rangle$.

The corresponding imbalance is

\[
I_r(t)=\frac{2}{L}\sum_{j=1}^{L}(-1)^{j+1}
\langle\psi_r(t)|S_j^z|\psi_r(t)\rangle,
\qquad I_r(0)=1.
\tag{2}
\]

The normalization makes the imbalance a dimensionless measure of the initial staggered pattern. The Hamiltonian conserves total $z$ magnetization, which is zero for these even-length initial states. This conservation does not fix the staggered magnetization: the transverse exchange terms transfer spin between neighboring sites and can change $I_r(t)$. The longitudinal interactions and random fields are diagonal in the initial spin basis. Thus the observable probes redistribution of the pattern within a fixed total-magnetization sector.

For window $a$, the realization-level quantity is

\[
X_{r,a}=\frac{1}{40}\int_{t_a}^{t_a+40} I_r(t)\,dt,
\qquad t_1=40,\quad t_2=80.
\tag{3}
\]

Exactly $n=32$ independent disorder realizations contribute at each $(L,W)$. Both windows use the same realization set within that point; different lengths use independently drawn samples. The reported mean is $\bar X_a=n^{-1}\sum_r X_{r,a}$, and its standard error of the mean (SEM) is obtained from the sample variance of these 32 realization means. Time points within a trajectory are not independent disorder samples. The supplied finite-system evolution is numerically converged, and the quoted errors describe disorder sampling rather than integration error. The Supplement develops the estimators and their consequences for comparisons.

## III. STRONGER RETENTION WITH PERSISTENT SIZE DEPENDENCE

Table I contains all supplied window averages. Every comparison at fixed length and window places $W=6$ above $W=3$. In the later window, the stronger-disorder means range from 0.600 to 0.450, whereas the weaker-disorder means range from 0.120 to 0.040. At the largest size, the difference in the reported central values is 0.410. A substantial fraction of the initial staggered pattern therefore remains in this window average at $W=6$.

**Table I.** Disorder-averaged imbalance for open spin chains, with one SEM over 32 realization means. The time windows have equal duration. Each row uses the same disorder realizations for both columns; samples at different lengths are independent.

| $W$ | $L$ | $\bar X_1$, $40\le t\le80$ | $\bar X_2$, $80\le t\le120$ |
|---:|---:|---:|---:|
| 3 | 12 | $0.180\pm0.020$ | $0.120\pm0.020$ |
| 3 | 16 | $0.150\pm0.018$ | $0.090\pm0.018$ |
| 3 | 20 | $0.120\pm0.017$ | $0.060\pm0.016$ |
| 3 | 24 | $0.100\pm0.016$ | $0.040\pm0.015$ |
| 6 | 12 | $0.620\pm0.025$ | $0.600\pm0.025$ |
| 6 | 16 | $0.580\pm0.024$ | $0.550\pm0.024$ |
| 6 | 20 | $0.540\pm0.023$ | $0.500\pm0.023$ |
| 6 | 24 | $0.500\pm0.022$ | $0.450\pm0.022$ |

The larger imbalance is accompanied by a systematic size drift in the central estimates. From $L=12$ to $24$, the $W=3$ means decrease by 0.080 in each window. At $W=6$, the decrease is 0.120 in the first window and 0.150 in the second. For the latter comparison, independent size ensembles give an endpoint-difference SEM of approximately 0.033. The later-window mean consequently loses one quarter of its $L=12$ value across the measured sizes. This endpoint comparison quantifies why a large residual imbalance alone is insufficient evidence of size stability.

Moving to the later window also lowers every central estimate. At $W=3$, the reduction is 0.060 for each length. At $W=6$, it increases from 0.020 at $L=12$ to 0.050 at $L=24$. These differences describe the evolution of window averages; they do not determine whether individual trajectories decay monotonically within either interval. In particular, the stronger-disorder signal remains large while its central values continue to change along both the time and size directions.

The paired nature of the windows matters for interpreting these temporal changes. Their difference has variance $\operatorname{Var}(\bar X_1)+\operatorname{Var}(\bar X_2)-2\operatorname{Cov}(\bar X_1,\bar X_2)$. The squared marginal SEMs estimate the first two terms, whereas the covariance is absent from the supplied summaries. A paired significance test therefore requires additional realization-level information. This statistical issue is distinct from the independent-size comparison and does not alter the observed ordering of the reported means.

## IV. CONCLUSION

The data support stronger finite-time retention of the Néel pattern at $W=6$ than at $W=3$ at all four measured lengths and in both windows. Within this range, a common, size-stable value is not established: the central estimates decrease with every size increment, including at the stronger disorder. The later-window central values are also lower, so their large amplitudes alone do not establish temporal saturation.

A nonzero infinite-time thermodynamic plateau concerns the continuation of both dependences beyond this finite domain. The table supplies neither a controlled extrapolation in length nor long-time saturation, so it leaves that limiting value undetermined. The physical conclusion within the measured domain is more specific: strong disorder preserves much more of the initial staggered pattern, but appreciable retention coexists with finite-size drift and changing window averages. Those are separate properties of the memory signal, and assessing a plateau requires their joint stabilization.

---

# Supplemental Material

## S1. Disorder mean and its standard error

For a fixed $(L,W)$ and window $a$, let $X_{r,a}$ be the time integral in Eq. (3). The independent sampling units are the $n=32$ field configurations. If their common disorder distribution has mean $\mu_a$ and variance $\sigma_a^2$, then independence gives

\[
\mathbb E[\bar X_a]=\mu_a,\qquad
\operatorname{Var}(\bar X_a)
=\frac{1}{n^2}\sum_{r=1}^{n}\operatorname{Var}(X_{r,a})
=\frac{\sigma_a^2}{n}.
\tag{S1}
\]

The unknown variance is estimated by

\[
s_a^2=\frac{1}{n-1}\sum_{r=1}^{n}(X_{r,a}-\bar X_a)^2,
\qquad e_a=\frac{s_a}{\sqrt n}.
\tag{S2}
\]

To verify the denominator, expand the residual sum as

\[
\sum_r(X_{r,a}-\bar X_a)^2
=\sum_r(X_{r,a}-\mu_a)^2-n(\bar X_a-\mu_a)^2.
\tag{S3}
\]

Its expectation is $n\sigma_a^2-\sigma_a^2=(n-1)\sigma_a^2$; hence $s_a^2$ is unbiased and $e_a^2$ estimates the variance of the sample mean. Table I reports $\bar X_a\pm e_a$. These bars are estimated standard errors, rather than specified-confidence intervals. No normal-distribution assumption is needed for Eq. (S1).

Time averaging precedes this sampling calculation. Spin values at different times share a trajectory and field configuration, so counting them as additional independent realizations would change the uncertainty estimate incorrectly. Numerical integration uncertainty is a separate quantity; convergence of the supplied evolution is stipulated, and Table I describes only disorder variability.

## S2. Uncertainty of the paired window difference

The same disorder realization supplies $X_{r,1}$ and $X_{r,2}$. Define the loss between windows by $D_r=X_{r,1}-X_{r,2}$, with sample mean $\bar D=\bar X_1-\bar X_2$. Introduce the sample covariance

\[
s_{12}=\frac{1}{n-1}\sum_r
(X_{r,1}-\bar X_1)(X_{r,2}-\bar X_2).
\tag{S4}
\]

Expanding the squared residuals of $D_r$ yields

\[
s_D^2=s_1^2+s_2^2-2s_{12},\qquad
e_D=\sqrt{\frac{s_D^2}{n}}
=\sqrt{e_1^2+e_2^2-\frac{2s_{12}}{n}}.
\tag{S5}
\]

A realization with unusually high imbalance in both windows contributes positive covariance, reducing the uncertainty of their difference. Negative covariance increases it. Replacing Eq. (S5) by addition of marginal variances assumes zero covariance, which is not implied by using disjoint time intervals. Independence holds between realizations, not between two observables evaluated on the same realization.

For nonzero marginal variances, write $\rho=s_{12}/(s_1s_2)$. Cauchy–Schwarz gives $-1\le\rho\le1$, so

\[
|e_1-e_2|\le e_D\le e_1+e_2.
\tag{S6}
\]

At $L=24,W=6$, the central window difference is 0.050 and both marginal SEMs are 0.022. Equation (S6) permits a difference SEM between 0 and 0.044; the marginal summaries alone select no value within this range. Thus an apparent window change cannot be assigned a paired significance from the displayed bars.

The 32 paired window means, retaining their realization identifiers, suffice to compute Eq. (S4). Alternatively, the sample covariance together with the unrounded marginal variances, or the sample variance of the 32 differences, determines Eq. (S5). Raw time trajectories are unnecessary for this uncertainty calculation once the paired window integrals are available. Distributional assessment or paired resampling would additionally use the realization-level differences.

## S3. Independent-size comparison

Different lengths use independent disorder ensembles. For the same $W$ and window, their sample-mean covariance therefore vanishes. The endpoint contrast $C=\bar X_{12,2}-\bar X_{24,2}$ has estimated SEM

\[
e_C=\sqrt{e_{12,2}^2+e_{24,2}^2}.
\tag{S7}
\]

At $W=6$, this gives $C=0.150$ and $e_C=\sqrt{0.025^2+0.022^2}\simeq0.033$, using the rounded table entries. This estimate characterizes the measured endpoint drift. It introduces no functional dependence on length and supplies no extrapolated plateau value.
