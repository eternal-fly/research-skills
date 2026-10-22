**Synthetic editorial test**

# Sampling cost of unbiased single-qubit measurement correction under known bit flips

## Abstract

Recovering an expectation value from a noisy quantum measurement requires accounting for both systematic attenuation and sampling uncertainty. For a single-qubit \(Z\) measurement subject to independent bit flips of known probability \(0\leq p<1/2\), we invert the attenuation at the observable level. The resulting estimator is exactly unbiased, with variance \([1-(1-2p)^2z^2]/[N(1-2p)^2]\) for expectation value \(z\) and \(N\) independent shots. A sufficient concentration bound has the same inverse-square dependence on the attenuation. At \(z=0\), the variance overhead relative to ideal measurements is \((1-2p)^{-2}\). The growing cost reflects the diminishing sensitivity of the measured probabilities to \(z\), which disappears at \(p=1/2\). Exact bias removal thus comes with a quantified amplification of sampling noise.

## I. INTRODUCTION

A noisy measurement can systematically underestimate the magnitude of an expectation value even when arbitrarily many shots are available. If the noise acts through a known attenuation, dividing the measured mean by that attenuation restores the correct expectation. This simple correction also rescales the fluctuations of every finite sample. Its statistical cost must therefore be assessed together with its removal of bias: an exact relation between ensemble averages does not make an individual estimate exact.

The single-qubit bit-flip channel makes this distinction explicit. A bit flip reverses the sign of the Pauli \(Z\) observable, so its average effect is to reduce the measurement contrast. The correction can be expressed directly in terms of this observable, without reconstructing the input state. The relevant resource question is how many independent measurements are sufficient to estimate the original expectation to a specified additive accuracy once that contrast has been reduced.

We address this question for a fixed, known channel and identically prepared, independent shots. The analysis connects the inverse observable response to an exact variance and a sufficient finite-sample confidence guarantee. A comparison at zero expectation isolates the variance overhead relative to ideal measurements. Calibration mismatch and the range of finite estimates then clarify the conditions under which exact unbiasedness applies. These results give one account of the cost of correcting a single observable: statistical fluctuations and errors in the assumed attenuation both pass through the same inverse factor.

## II. MEASUREMENT MODEL AND OBSERVABLE INVERSION

Let \(\rho\) be an arbitrary single-qubit state and let

\[
z=\operatorname{Tr}(\rho Z),\qquad -1\leq z\leq1.
\tag{1}
\]

Before measuring \(Z\), the state undergoes the channel

\[
\mathcal E_p(\rho)=(1-p)\rho+pX\rho X,
\qquad a=1-2p>0.
\tag{2}
\]

The known probability \(p\) is fixed across shots, and the bit flips and measurement outcomes are independent between preparations. Since \(XZX=-Z\), the channel transforms the observable as \(\mathcal E_p^\dagger(Z)=aZ\). Consequently, each recorded outcome \(Y_i\in\{+1,-1\}\) has mean \(m=az\). This attenuation is the entire channel response relevant to the specified estimation task.

The inverse response suggests assigning the corrected value \(Y_i/a\) to each outcome. With \(\bar Y=N^{-1}\sum_{i=1}^{N}Y_i\), the estimator is

\[
\widehat z=\frac{\bar Y}{a},
\qquad \mathbb E[\widehat z]=z.
\tag{3}
\]

Equation (3) is exact for every input state and every positive integer \(N\) under the stated channel and sampling assumptions. It is an assertion about repeated sampling, rather than equality of a finite realization with \(z\). The correction changes the numerical values assigned to the outcomes; it leaves their probabilities unchanged.

Those probabilities also determine the uncertainty. Because \(Y_i^2=1\), the variance of a single outcome is \(1-a^2z^2\). Independence reduces the variance of the sample mean by \(N\), while inversion multiplies it by \(a^{-2}\). Hence

\[
\operatorname{Var}(\widehat z)
=\frac{1-a^2z^2}{Na^2}.
\tag{4}
\]

The numerator contains the fluctuations of the actual binary observations, and the denominator contains the squared inverse response. In particular, removal of the attenuation in the mean amplifies the standard deviation of the raw sample mean by \(1/a\).

## III. SAMPLING COST AND IDENTIFIABILITY

A confidence guarantee translates this amplification into a sufficient shot budget. For a prescribed additive tolerance \(\eta>0\), the event \(|\widehat z-z|\geq\eta\) is equivalent to \(|\bar Y-m|\geq a\eta\). Applying Hoeffding's inequality to independent outcomes in \([-1,1]\) gives

\[
\Pr\!\left(|\widehat z-z|\geq\eta\right)
\leq2\exp\!\left[-\frac{Na^2\eta^2}{2}\right].
\tag{5}
\]

Thus, for a target failure probability \(0<\alpha<1\), it is sufficient to take

\[
N\geq\frac{2\log(2/\alpha)}{(1-2p)^2\eta^2},
\tag{6}
\]

rounding up to an integer when choosing the shot count. This guarantee holds uniformly over the input expectation. Equation (6) is a sufficient bound obtained from a bounded-variable concentration inequality, not an optimal sample-complexity statement. Its independence from \(z\) is useful when the expectation to be measured is initially unknown; the exact variance in Eq. (4) retains the state dependence.

An ideal \(Z\) measurement on \(\rho\) has sample-mean variance \((1-z^2)/N\). At \(z=0\), the ideal variance is \(1/N\), whereas the corrected noisy estimator has variance \(1/(Na^2)\). Their ratio at the same shot count is therefore

\[
R(p)=\frac{1}{(1-2p)^2}.
\tag{7}
\]

**TABLE I.** Variance overhead \(R(p)\) of the unbiased corrected estimator relative to the ideal estimator at \(z=0\), for equal numbers of independent shots. Values are evaluations of Eq. (7).

| Bit-flip probability \(p\) | Variance overhead \(R(p)\) |
|---:|---:|
| 0.05 | 1.2345679012 |
| 0.10 | 1.5625 |
| 0.20 | 2.7777777778 |
| 0.40 | 25 |

The increase in Table I is a cost in shots for matching the ideal variance at this expectation. For example, at \(p=0.40\), the corrected estimator requires 25 times as many shots to attain the same variance. Although the raw mean is already unbiased when \(z=0\), the correction is defined to recover all possible values of \(z\), and its rescaling still acts on the fluctuations at this point.

The divergence as \(p\) approaches \(1/2\) has an identifiable statistical origin. The probabilities \(\Pr(Y_i=\pm1)=(1\pm az)/2\) become less sensitive to \(z\) as \(a\) decreases. At \(p=1/2\), both probabilities equal \(1/2\) for every input expectation. The specified measurement record then contains no information that distinguishes different values of \(z\), and division by the attenuation is undefined. This loss of identifiability concerns the chosen observable and measurement record.

## IV. CALIBRATION AND FINITE ESTIMATES

Exact unbiasedness depends on using the actual attenuation. If a fixed value \(p_0\in[0,1/2)\) is used in its place, the corrected estimate has bias

\[
\mathbb E\!\left[\frac{\bar Y}{1-2p_0}\right]-z
=\frac{2(p_0-p)z}{1-2p_0}.
\tag{8}
\]

This expression separates finite-shot fluctuations from a systematic calibration mismatch. The mismatch bias is independent of \(N\); increasing the number of shots does not remove it. Equation (8) treats \(p_0\) as fixed. A value estimated from calibration data is a random quantity, and its uncertainty requires the joint sampling model of that calibration and the measurement record. The known-channel guarantee in Eq. (6) applies with the true fixed \(p\).

The corrected estimate can also lie outside the physical interval \([-1,1]\), since its possible range is \([-1/a,1/a]\). Such values are realizations of an unbiased estimator, not physical expectation values assigned to a state. Clipping the estimate to \([-1,1]\) changes its sampling distribution and generally introduces bias. The Supplement gives an explicit boundary-state argument showing why clipping cannot retain the stated unbiasedness for all inputs.

## V. CONCLUSION

For independent single-qubit \(Z\) measurements with a known bit-flip probability below \(1/2\), inversion of the observable attenuation gives an exactly unbiased estimator. The same inverse factor amplifies sampling fluctuations, producing the variance in Eq. (4), the sufficient shot budget in Eq. (6), and the overhead in Table I. These quantities connect correction accuracy to the sensitivity of the measured probabilities. As that sensitivity vanishes, the cost grows, and at \(p=1/2\) the expectation becomes unidentifiable from the specified data. Calibration and estimator postprocessing belong to this statistical account: fixed calibration mismatch leaves a bias, while clipping changes the unbiased estimator. Exact removal of a known bias therefore restores the ensemble mean with an explicit cost in sampling uncertainty.

---

# Supplemental Material

## S1. Outcome distribution, unbiasedness, and variance

Write \(a=1-2p>0\). Cyclicity of the trace and \(XZX=-Z\) give

\[
\operatorname{Tr}[\mathcal E_p(\rho)Z]
=(1-p)\operatorname{Tr}(\rho Z)
+p\operatorname{Tr}(\rho XZX)=az.
\tag{S1}
\]

For a binary outcome, normalization and this mean uniquely fix

\[
\Pr(Y_i=y)=\frac{1+yaz}{2},\qquad y\in\{-1,+1\}.
\tag{S2}
\]

Both probabilities are nonnegative for the stipulated state and channel. Averaging identically distributed outcomes yields \(\mathbb E[\bar Y]=az\), and dividing by the known positive \(a\) proves \(\mathbb E[\widehat z]=z\).

Since \(\mathbb E[Y_i^2]=1\), each outcome has variance \(1-a^2z^2\). Independent shots have zero cross-covariances, so

\[
\operatorname{Var}(\widehat z)
=\frac{1}{N^2a^2}\sum_{i=1}^{N}\operatorname{Var}(Y_i)
=\frac{1-a^2z^2}{Na^2}.
\tag{S3}
\]

Thus independence supplies the \(1/N\) variance reduction. For ideal measurements, setting \(p=0\) gives \((1-z^2)/N\); at \(z=0\), the ratio of corrected to ideal variance is \(a^{-2}\). This ratio is evaluated at the same shot count and expectation in Table I.

## S2. Sufficient concentration bound

For independent variables \(Y_i\in[-1,1]\), the two-sided Hoeffding bound is

\[
\Pr(|\bar Y-\mathbb E\bar Y|\geq t)
\leq2\exp\!\left[-\frac{2N^2t^2}{\sum_i(1-(-1))^2}\right]
=2e^{-Nt^2/2}.
\tag{S4}
\]

The event of interest has \(t=a\eta\), because \(\widehat z-z=(\bar Y-az)/a\). Substitution gives Eq. (5). Requiring its right-hand side to be at most \(\alpha\), with \(\eta>0\) and \(0<\alpha<1\), gives

\[
N\geq\frac{2\log(2/\alpha)}{a^2\eta^2}.
\tag{S5}
\]

Choosing the ceiling of this expression is sufficient. The bound uses only independence and the range of the outcomes, so it is uniform in \(z\). It supplies an upper bound on the shot count needed for this guarantee; the derivation does not establish a matching necessary count or optimality.

## S3. Bias from fixed calibration mismatch

Let \(a_0=1-2p_0>0\) be a fixed correction factor, while the actual channel still has attenuation \(a\). Then

\[
\mathbb E[\bar Y/a_0]-z
=\left(\frac{a}{a_0}-1\right)z
=\frac{2(p_0-p)z}{1-2p_0}.
\tag{S6}
\]

The bias vanishes for correct calibration or for \(z=0\). Otherwise it persists as the shot count increases. If the denominator instead contains a random estimate of \(p\), its inverse remains inside the expectation; inserting a mean calibration value into Eq. (S6) does not in general give the resulting bias. The fixed-parameter calculation therefore keeps channel knowledge distinct from calibration estimation.

## S4. Range and clipping

The sample mean lies in \([-1,1]\), so \(\widehat z\) lies in \([-1/a,1/a]\). For \(p>0\), an all-positive record gives \(\widehat z=1/a>1\), and an all-negative record gives \(-1/a<-1\). Equation (S2) assigns positive probability to both records for every finite \(N\). An estimator can take these values while its expectation remains the physical value \(z\).

Define the clipped estimate by \(\widetilde z=\max[-1,\min(1,\widehat z)]\). Clipping is nonlinear, so the unbiasedness of \(\widehat z\) does not transfer to \(\widetilde z\). In particular, take \(z=1\) and \(0<p<1/2\). Every clipped outcome is at most one, whereas the all-negative record has probability \(p^N>0\) and gives \(\widetilde z=-1\). Consequently,

\[
\mathbb E[\widetilde z]\leq1-2p^N<1=z.
\tag{S7}
\]

This example establishes loss of unbiasedness for the clipped procedure as a general estimator. Special inputs can retain zero bias, but exact unbiasedness for all input states belongs to the unmodified estimator in Eq. (3).
