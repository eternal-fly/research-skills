# Focused prose behavior review

Date 2026-10-28. Base commit `1e87420fdecc3463197ba99192142c4cd52b5e54`.

Five distinct synthetic editing requests were each run once with unchanged 1.2.0 active instructions and once with revised 1.2.1 guidance. Each of the ten comparison calls used a fresh agent context, gpt-6.1-sol at high reasoning effort, the designated skill and relevant references, without other writing skills or browsing. The requests did not repeat the new punctuation and attribution rules. This tests whether the skill supplies those rules during ordinary editing.

Five preliminary baseline calls had incorrectly escaped TeX commands in the input fixtures. Those inputs were corrected and all five baseline cases rerun. The preliminary calls are excluded from the comparison and retained only in the local audit. The public comparison inputs are in [the cases directory](../../tests/prose-conventions-cases/); baseline and revised output files here are unedited agent outputs, with SHA-256 fingerprints in [results.json](results.json).

The integrator read all ten comparison outputs in full. Literal scans were used only to locate possible issues; mathematical colons, citation keys, bibliography fields and heading commands were inspected in context.

| Case | 1.2.0 observation | 1.2.1 observation | Preserved content |
|---|---|---|---|
| English PRL body | Retains online-preprint wording | Uses earlier work and recent work by verified authors | Principal heading, common/local noise distinction, fixed generator and decay law |
| English Supplement | Already meets the requested style | Meets the requested style | Known fixed flip rate, independence, exact variance, clipping qualification, mapping and ratio notation, citation key |
| Chinese body and Supplement | Retains online-preprint wording and identifier | Uses existing research and the named authors' recent study | Four sizes, uncertainty, null comparison and covariance condition |
| Incomplete attribution and bibliography | Retains preprint and journal-article labels and identifier | Uses neutral earlier work; no invented author or recency | Conjecture/theorem distinction, finite-size quantifier, bibliography verbatim |
| PRL heading roles | Retains online-preprint wording and identifier | Removes status wording and identifier; retains heading macros | Principal and Note added headings, phase mechanism, constant populations, decay rate and counterexample |

Four baseline outputs retain at least one targeted literature-wording violation; none of the five revised outputs does. Both conditions already avoid explanatory dashes and prose colons after editing, apart from colons inside retained identifiers. This sample therefore does not demonstrate a punctuation improvement over 1.2.0. It does confirm that the revised guidance can remove the requested wording while preserving the tested scientific and citation roles.

The five cases are varied applications, not five repeated trials of each prompt. They are short synthetic passages rather than complete manuscripts, real literature verification, a statistical success-rate estimate, or a causal model-quality study. No TeX compilation or new heading-render inspection was performed for these snippets. The unchanged 1.2.0 full-manuscript evidence remains historical.
