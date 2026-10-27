# Synthetic editing fixture

All names, citation keys, identifiers and scientific findings in this fixture are synthetic test data, not real literature. Treat the supplied metadata as facts of this editing exercise; do not browse or invent sources. The exercise date is 2026-10-28.

Use the specified APS Quantum Writing skill to edit the passage into ready-to-use manuscript prose in the requested language. Preserve the scientific meaning, conditions, uncertainty and citation keys. Keep reference metadata separate from the prose and unchanged where supplied. Deliver the revised passage and any supplied bibliography block only, without an editing report. Follow the skill's normal editorial conventions. Avoid unrelated changes.

## Chinese main text and supplementary paragraph

Write in Chinese. Retain the citation commands and supplied numerical information. Keep these as two paragraphs under the supplied Markdown headings.

Metadata supplied for editing: `wang2023` is a journal article from 2023; `li2026` is an online preprint by Li and Zhou, posted in October 2026, identifier arXiv:2610.00001 (synthetic).

### 正文
已发表的文章 \cite{wang2023} 给出了一个结论：有限尺寸中的慢弛豫可以形成长寿命平台。李和周的在线预印本 arXiv:2610.00001 \cite{li2026} 指出了另一种解释——平台可能来自有限观测窗口。我们的数据覆盖 $L=12,16,20,24$——这些有限尺寸结果用于比较两种解释。差值为 $0.01\pm0.03$，两种制备没有统计上可分辨的差异。

### 附加材料
误差估计必须保留一个条件：两个时间窗使用相同的无序样本。差值方差满足 $\operatorname{Var}(A-B)=\operatorname{Var}(A)+\operatorname{Var}(B)-2\operatorname{Cov}(A,B)$——忽略协方差会改变比较的不确定度。

