\subsection{Calibrated readout}
Earlier work \cite{liu:2025} motivates correcting the measured mean by dividing it by the readout visibility. Let $X\in\{-1,1\}$ have mean $z$, and let independent readout flips occur with a fixed, known probability $0\le p<1/2$. The recorded outcome $Y$ then has mean $(1-2p)z$. The correction map is $f:\mathbb R\to\mathbb R$, $f(x)=x/(1-2p)$, and the sampling ratio is $N_1:N_2=1:2$.

For $N$ independent measurements, the corrected estimator $\widehat z=\overline Y/(1-2p)$ is unbiased. Since $Y^2=1$, its exact variance is
\[
\operatorname{Var}(\widehat z)=\frac{1-(1-2p)^2z^2}{N(1-2p)^2}.
\]
These results use the fixed, known value of $p$ and the independence of the shots. Clipping $\widehat z$ to $[-1,1]$ need not preserve its expectation, so the clipped estimator need not be unbiased.
