**Synthetic editorial test**

# Sampling cost of unbiased single-qubit measurement correction under known bit-flip noise

## Abstract

A known bit-flip channel attenuates a single-qubit measurement signal, so its mean can be restored by inverting the observable response. For independent shots and a fixed known flip probability \(0\leq p<1/2\), this inversion gives an exactly unbiased estimator of the input \(Z\) expectation. The same inverse response amplifies sampling fluctuations: the estimator has variance \([1-(1-2p)^2z^2]/[N(1-2p)^2]\), where \(z\) is the target expectation and \(N\) is the number of shots. A bounded-outcome concentration inequality yields a sufficient shot count for a prescribed error and failure probability. At zero expectation, the variance overhead relative to ideal measurement is \((1-2p)^{-2}\). Its divergence accompanies the loss of information about \(z\) at \(p=1/2\), while a fixed calibration error leaves a residual bias that additional shots do not remove.

## I. INTRODUCTION

A measurement affected by a known noise channel can retain enough information to reconstruct an ideal expectation value. The reconstruction nevertheless acts on a finite sample of random outcomes. Correcting the relation between the measured and target means therefore raises a separate question: how much sampling is required to determine the corrected value with a specified precision? Even a single-qubit measurement exposes this distinction because a channel can suppress the mean without suppressing the fluctuations that must be resolved.

Consider a measurement of the Pauli observable \(Z\) after an independent bit flip. A flip reverses the sign of the ideal outcome, reducing the average signal by a known factor. Dividing by that factor restores the target mean. It also enlarges every fluctuation of the sample mean, so the absence of systematic attenuation does not imply a narrow distribution of corrected estimates. The relevant comparison must specify both the observable being estimated and the number of measurement shots.

Here the task is to estimate one expectation value for an arbitrary input state through a fixed, known bit-flip channel. The channel acts on this observable through a scalar attenuation, making it possible to obtain the exact estimator variance directly from the two-outcome measurement statistics. This calculation identifies the sampling overhead, and a concentration bound converts it into a sufficient resource allocation at a chosen accuracy. The same response factor also connects sampling sensitivity to identifiability and to the residual bias produced by a fixed error in the correction parameter.

## II. OBSERVABLE RESPONSE AND UNBIASED CORRECTION

Let \(\rho\) be an arbitrary single-qubit density operator and

\[
z=\operatorname{Tr}(\rho Z),\qquad -1\leq z\leq 1.
\tag{1}
\]

Each independently prepared copy passes through

\[
\mathcal E_p(\rho)=(1-p)\rho+pX\rho X,
\qquad 0\leq p<\tfrac12,
\tag{2}
\]

with the same known probability \(p\). Measuring \(Z\) then gives independent, identically distributed outcomes \(Y_i\in\{+1,-1\}\). Define the positive response factor \(a=1-2p\). Since \(XZX=-Z\), the channel transforms the measured observable into \(\mathcal E_p^\dagger(Z)=aZ\), and hence

\[
m=\mathbb E[Y_i]=az.
\tag{3}
\]

This relation is sufficient for the estimation task: the channel response for \(Z\) can be inverted without reconstructing the other components of \(\rho\). With \(N\geq1\) shots and sample mean \(\bar Y=N^{-1}\sum_{i=1}^{N}Y_i\), the corrected estimate is

\[
\widehat z=\frac{\bar Y}{a},
\qquad \mathbb E[\widehat z]=z.
\tag{4}
\]

Unbiasedness here is an exact statement about the expectation over repeated samples at fixed \(\rho\), \(p\), and \(N\). A particular sample still fluctuates. The parameter \(p\) is supplied as a known channel property; the shot count \(N\) counts the measurements used to estimate \(z\).

## III. VARIANCE AND SHOT OVERHEAD

The magnitude of those fluctuations follows from the outcome alphabet. Because \(Y_i^2=1\), a single shot has variance \(1-m^2\). Independence reduces the sample-mean variance by \(N\), and division by \(a\) multiplies that variance by \(a^{-2}\). Thus

\[
\operatorname{Var}(\widehat z)
=\frac{1-a^2z^2}{Na^2}.
\tag{5}
\]

Equation (5) separates the fluctuations present in the observed outcomes from their amplification during correction. It also shows why exact removal of the mean bias is compatible with substantial uncertainty. For fixed \(p<1/2\), increasing \(N\) reduces the corrected variance in inverse proportion to the number of shots, with a coefficient set by the channel response and the state.

An ideal measurement on the same input, using the same number of independent shots, has sample-mean variance \((1-z^2)/N\). At \(z=0\), both the ideal and noisy raw outcomes are equiprobable, and the ideal variance is \(1/N\). The ratio of corrected to ideal variances is consequently

\[
R(p)=\left.\frac{\operatorname{Var}(\widehat z)}
{\operatorname{Var}(\bar Y_{\mathrm{ideal}})}\right|_{z=0}
=\frac{1}{(1-2p)^2}.
\tag{6}
\]

**TABLE I.** Variance overhead \(R(p)\) at \(z=0\), relative to ideal measurement with the same shot count. Values are evaluations of Eq. (6).

| Bit-flip probability \(p\) | Variance overhead \(R(p)\) |
|---:|---:|
| 0.05 | 1.2345679012 |
| 0.10 | 1.5625 |
| 0.20 | 2.7777777778 |
| 0.40 | 25 |

The increase in Table I is controlled by the shrinking response factor. At \(p=0.40\), for example, the corrected variance is 25 times the ideal variance at equal shot count. Matching the ideal variance at \(z=0\) therefore requires 25 times as many shots. This comparison concerns the same target expectation and precision; the listed factor is not a state-independent variance ratio. At \(p=0\), the response factor is unity and the corrected estimator reduces to the ordinary ideal sample mean.

## IV. FINITE-SAMPLE PRECISION AND IDENTIFIABILITY

A variance describes mean-square fluctuations, whereas a prescribed failure probability requires control of the distribution's tails. For any \(\eta>0\), Hoeffding's inequality for independent outcomes in \([-1,1]\) gives

\[
\Pr\!\left(|\widehat z-z|\geq\eta\right)
\leq 2\exp\!\left[-\frac{Na^2\eta^2}{2}\right].
\tag{7}
\]

The response enters because an error \(\eta\) in the target expectation corresponds to an error \(a\eta\) in the measured mean. For a requested failure probability \(0<\alpha<1\), choosing an integer shot count satisfying

\[
N\geq\frac{2\log(2/\alpha)}{(1-2p)^2\eta^2}
\tag{8}
\]

is sufficient to make the right-hand side of Eq. (7) at most \(\alpha\). Equation (8) is a sufficient, state-independent allocation obtained from bounded outcomes. The exact variance in Eq. (5) retains the dependence on \(z\) that this uniform bound discards.

Both expressions become costly as \(p\) approaches \(1/2\): increasingly small differences in the measured mean must resolve the same difference in the target expectation. At \(p=1/2\), the measurement law is \(\Pr(Y_i=+1)=\Pr(Y_i=-1)=1/2\) for every \(z\). The \(Z\)-measurement records then contain no information that distinguishes different target expectations. The singular inverse response thus corresponds to loss of identifiability for this task at the endpoint.

## V. CALIBRATION AND THE RANGE OF FINITE ESTIMATES

The correction depends on the parameter used to invert the response. If the true channel has probability \(p\) but a fixed value \(0\leq p_0<1/2\) is used in the denominator, the residual bias is

\[
\mathbb E\!\left[\frac{\bar Y}{1-2p_0}\right]-z
=\frac{2(p_0-p)z}{1-2p_0}.
\tag{9}
\]

All expectations in Eq. (9) average over measurement shots with \(p\) and \(p_0\) held fixed. A mismatch can therefore persist as the shot count grows. The formula makes calibration accuracy part of the interpretation of an apparently precise corrected value, and it separates this fixed bias from the sampling variance of the known-channel estimator.

For \(p>0\), finite estimates can also lie outside the physical interval \([-1,1]\), since division by \(a<1\) enlarges the range of \(\bar Y\). Such values are realizations of a statistical estimator whose mean is a physical expectation. Clipping them to the physical interval changes the estimator and generally destroys its exact unbiasedness. The Supplement derives this effect together with Eqs. (4), (5), (8), and (9).

## VI. CONCLUSION

For a known independent bit-flip channel, inversion of the single-observable response removes the bias of a \(Z\)-expectation estimate exactly. Its sampling cost is fixed by the same response: the corrected variance is given by Eq. (5), and Eq. (8) supplies a shot allocation for a prescribed error probability. At zero expectation, the cost relative to ideal measurement grows as \((1-2p)^{-2}\), reaching a singular endpoint when the measurement ceases to identify \(z\). Calibration mismatch adds a distinct, persistent bias. Together these relations quantify what observable correction accomplishes and how the precision of the recovered expectation depends on sampling and channel knowledge.

---

# Supplemental Material

## S1. MEASUREMENT LAW, UNBIASEDNESS, AND VARIANCE

For the arbitrary input \(\rho\), write \(z=\operatorname{Tr}(\rho Z)\) and fix the known channel parameter \(0\leq p<1/2\). Cyclicity of the trace and \(XZX=-Z\) give

\[
\operatorname{Tr}[Z\mathcal E_p(\rho)]
=(1-p)z+p\operatorname{Tr}(XZX\rho)
=(1-2p)z=az.
\tag{S1}
\]

The projectors of the measured observable are \((I\pm Z)/2\). The resulting single-shot probabilities are therefore

\[
\Pr(Y_i=\pm1)=\frac{1\pm az}{2}.
\tag{S2}
\]

Take \(N\) independent, identically prepared shots, with sample mean \(\bar Y=N^{-1}\sum_iY_i\), and define \(\widehat z=\bar Y/a\). The probabilities in Eq. (S2) determine both moments needed for this estimator. In particular, \(\mathbb E[Y_i]=az\) and \(\mathbb E[Y_i^2]=1\). Linearity of expectation gives

\[
\mathbb E[\widehat z]
=\frac{1}{Na}\sum_{i=1}^{N}\mathbb E[Y_i]=z.
\tag{S3}
\]

For independent shots, the cross covariances vanish. Consequently,

\[
\operatorname{Var}(\widehat z)
=\frac{1}{N^2a^2}\sum_{i=1}^{N}\operatorname{Var}(Y_i)
=\frac{1-a^2z^2}{Na^2}.
\tag{S4}
\]

Both steps hold for every finite positive integer \(N\). Known \(a>0\) ensures that the division is defined, while independence supplies the variance reduction by \(N\).

## S2. SUFFICIENT CONCENTRATION BOUND

Hoeffding's inequality for the independent variables \(Y_i\in[-1,1]\), each with interval length two, yields

\[
\Pr(|\bar Y-m|\geq t)
\leq2\exp\!\left[-\frac{2N^2t^2}{4N}\right]
=2e^{-Nt^2/2},\qquad t>0.
\tag{S5}
\]

Choose an error tolerance \(\eta>0\) and a failure probability \(0<\alpha<1\). Since \(m=az\) and \(a>0\), the events \(|\widehat z-z|\geq\eta\) and \(|\bar Y-m|\geq a\eta\) are identical. Substitution of \(t=a\eta\) proves Eq. (7). Requiring its upper bound to be at most \(\alpha\) gives

\[
\frac{Na^2\eta^2}{2}\geq\log\frac{2}{\alpha},
\tag{S6}
\]

which is Eq. (8); the next integer can be used when its right-hand side is nonintegral. This is a sufficient guarantee uniform over input states. It is derived from the bounded outcome range, rather than an optimization of the sample complexity.

## S3. FIXED CALIBRATION MISMATCH

Let the true attenuation remain \(a=1-2p\), but use a fixed correction parameter \(0\leq p_0<1/2\), giving a positive denominator \(a_0=1-2p_0\). The measured sample still has expectation \(az\), so

\[
\mathbb E\!\left[\frac{\bar Y}{a_0}\right]-z
=\left(\frac{a}{a_0}-1\right)z
=\frac{2(p_0-p)z}{1-2p_0}.
\tag{S7}
\]

The bias vanishes for correct calibration and also at \(z=0\). Otherwise it is independent of \(N\). Equation (S7) concerns two fixed channel parameters. Substituting an estimated probability would make the denominator random; its expectation would then depend on the calibration estimator's distribution and any statistical dependence on the measurement shots.

## S4. FINITE ESTIMATES AND CLIPPING

The sample mean lies in \([-1,1]\), whereas the corrected estimator lies in \([-1/a,1/a]\). For \(0<p<1/2\), this larger interval extends beyond the spectrum of \(Z\). An all-positive sample, for example, gives \(\widehat z=1/a>1\) and occurs with probability \([(1+az)/2]^N>0\). The estimator's range thus differs from the allowed range of its target.

To see explicitly why clipping changes unbiasedness, define \(C(x)=\min(1,\max(-1,x))\). For one shot and \(0<p<1/2\),

\[
C(\widehat z)=C(Y_1/a)=Y_1,
\qquad \mathbb E[C(\widehat z)]=az.
\tag{S8}
\]

The clipped estimator has bias \((a-1)z=-2pz\), which is nonzero when \(z\ne0\). This example directly establishes that clipping does not preserve the unbiasedness guarantee. The expectation in Eq. (S3) relies on applying the same linear inverse response to every sample, including those producing values outside the physical interval. Unbiasedness refers to averaging the numerical estimates over repeated samples. It does not impose a physical-state interpretation on each realized estimate; imposing that interval constraint by clipping introduces a different, nonlinear statistical rule.
