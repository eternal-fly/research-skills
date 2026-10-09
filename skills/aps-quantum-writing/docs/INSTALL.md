# Installation and updates

## Choose the simplest route

This is a file-based agent skill, not a desktop executable or a Python package. No account credentials, background service, browser extension, or API key are bundled. Review [the license](../LICENSE) before using it.

### A. Versioned ZIP (recommended)

1. Download `aps-quantum-writing-1.0.0.zip` and its SHA-256 checksum from the repository's release.
2. Verify the checksum using your operating system's checksum utility.
3. Extract the ZIP. The resulting folder must contain `SKILL.md` directly, with `references`, `assets`, `scripts`, `docs`, and the license beside it.
4. Place the complete folder in a location supported by your agent, or use the manual route below.

Do not place the ZIP itself in a skill folder and expect local folder discovery to unpack it. Avoid the accidental double nesting `aps-quantum-writing/aps-quantum-writing/SKILL.md`.

### B. Codex local skill

For a project-local installation, copy the extracted folder to:

```text
<your-project>/.agents/skills/aps-quantum-writing/SKILL.md
```

For a personal installation, use:

```text
<your-home>/.agents/skills/aps-quantum-writing/SKILL.md
```

Keep every sibling file and directory from the release. Confirm the skill appears in your client's skill list, then invoke it explicitly, for example `$aps-quantum-writing`. Restart the client if discovery has not refreshed. Avoid installing two copies with the same skill name in overlapping scopes.

These are local skill-folder instructions. They do not register a hosted plugin or publish anything to an application marketplace. Current discovery details: [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills).

### C. Manual, client-neutral use

Open the repository or extracted directory in an agent environment that can read local files. Ask the agent:

```text
Read SKILL.md from this folder. Use its relevant branch for my next task,
loading the linked reference files when required.
```

A chat interface that cannot read the folder cannot automatically follow its relative links. Provide the required files through that interface's supported file mechanism. Simply pasting the entry file is not equivalent to making its referenced files available.

### D. Source checkout

Clone the public repository into a new directory. Use the `v1.0.0` tag for a reproducible released snapshot; use the default branch only if you intentionally want subsequent development. In the multi-skill repository, use `skills/aps-quantum-writing` as the skill folder. Do not run an unreviewed remote shell installer.

## Requirements by task

| Task | Requirements |
|---|---|
| Planning, prose, review | An agent that can read Markdown and supporting files |
| Verify current journal rules and references | Appropriate permitted access to official sources |
| Run example plots/tests | Python and dependencies in `requirements.txt` |
| Compile heading examples | Working pdfLaTeX, REVTeX 4.2f, etoolbox |
| Edit an actual manuscript | Its source, bibliography, figures, and the relevant build toolchain |

An unavailable tool should produce a specific unverified-step note. It must not lead to fabricated references, results, plots, or claims of successful compilation.

## Optional Python setup

Create an isolated environment using your usual environment manager, then from the extracted root:

```sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Dependencies are optional for instruction-only use. Versions actually tested are listed in the validation report; an untested platform/version combination is not certified. For a read-only home directory, set `MPLCONFIGDIR` and `XDG_CACHE_HOME` to writable temporary directories before running plotting tools.

## Verify installation

Ask for a short plan for a PRL manuscript with an unheaded introduction. A correct response preserves the unheaded choice, identifies the central scientific question, and distinguishes selected PRL run-in headings from other Letters' period-ended headings. The skill must not insert a fixed chapter list.

For a stronger check, follow [validation](VALIDATION.md). A discovery check is not a scientific or visual quality audit.

## Updates and removal

Before updating, move or copy your private edits outside the installed folder as a backup. Extract the new release into a fresh directory, compare the changelog and license, and replace the old folder only after reviewing the differences. Do not blindly merge old and new trees: deleted or renamed references can survive an overlay.

To stop using the skill, remove or disable that installed copy through your client. This does not delete manuscripts or data stored elsewhere. Keep research outputs outside the skill's installation directory.
