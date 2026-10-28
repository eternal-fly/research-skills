# v1.2.1 package refresh

Date 2026-10-28 (Asia/Shanghai). VERSION remains 1.2.1. The author requested that the existing GitHub Release installation package include the [short-format wording refinement](PROSE-FOLLOWUP-2026-10-28.md) already committed as `733ae812392f6491d1ff126f30e4710b195c64e2`.

The refresh replaces `aps-quantum-writing-1.2.1.zip`, `research-skills-1.2.1-source.zip` and the release-level `SHA256SUMS`. The heading example PDF and historical heading-validation archive retain their original bytes. The Release notes identify the exact package source commit, checksums and successful refresh workflow run.

The Git tag `v1.2.1` remains at `bd2f9225c866f07117bb54cdda9243dc53935db0`. GitHub's automatic "Source code" ZIP and tarball therefore remain the initial snapshot. The attached `research-skills-1.2.1-source.zip` is the source for this refreshed installation package. The internal skill manifest covers every shipped skill file except itself.

## Validation boundary

The refresh uses the unchanged frozen 1.2.1 builder. Local checks and the release workflow run the 27-method skill suite, the four builder regression methods, package checksum and byte comparisons, and the skill suite from a fresh extraction. The successful workflow is the publication receipt; its logs and retained audit artifact record the actual results, previous release metadata and checksums, and downloaded replacement assets. The workflow stops on an unexpected release or tag, backs up the original five assets before replacing three, and downloads the final assets for byte comparison.

No new behavioral model calls, manuscript review, literature review, figure rendering, REVTeX compilation or typography assertions are performed for this packaging refresh. The [short-format source-validation record](../evidence/short-format-followup-2026-10-28/validation.json), [initial v1.2.1 report](RELEASE-1.2.1.md), and all earlier evidence retain their original execution scope. The source-validation record's statement that assets were unchanged describes the earlier source-only step, not the later package refresh.

## Previous package identity

Before replacement, release ID `425780927` contained the following SHA-256 hashes. These identify the original package, not the refreshed download.

| Asset | Original SHA-256 |
| --- | --- |
| `aps-quantum-writing-1.2.1.zip` | `c260c70f8aa9f789655260f17c06f93e32205fb3f8f0cdaed255a734fd1133c5` |
| `research-skills-1.2.1-source.zip` | `a2e16dfbfda9b564564e26fca359506ce3a272746804cf976b1def99201503a5` |
| `SHA256SUMS` | `ffff29a02d146fa927ce3ca2edc5bfc922583a0cf62de64482f692a0b6a2282b` |

Use the checksum file downloaded alongside the refreshed installation ZIP. The initial release's recorded hashes remain historical and are not relabeled as the refreshed package's hashes.
