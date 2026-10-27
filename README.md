# Research Skills

Reusable research workflows by **Luofei Wang**.

This public repository collects file-based agent skills for scientific work. Each skill lives in its own directory, with instructions, documentation, examples, and explicit licensing. Read the applicable license before using, modifying, or redistributing any skill.

## Skill catalog

| Skill | What it covers | Version | License |
|---|---|---|---|
| [APS Quantum Writing](skills/aps-quantum-writing/README.md) | Manuscript planning, scientific writing, figures, and journal-specific typography for seven APS journals | 1.2.1 | [Noncommercial source-available](skills/aps-quantum-writing/LICENSE) |

**Publicly readable does not mean unrestricted open source.** APS Quantum Writing permits noncommercial use and private modifications, with restrictions on commercial use and redistribution/repackaging. Its research-output, third-party, and platform exceptions are described in the license. Future skills may use different terms.

## Install a skill

Download its versioned ZIP from this repository's **Releases**, verify the published checksum, and follow the skill's installation guide. For the current release, see [APS installation](skills/aps-quantum-writing/docs/INSTALL.md).

If working from a source checkout, the skill folder is `skills/aps-quantum-writing`, not this repository's root. Keep the complete skill directory together. The top-level repository ZIP is a source archive, not the same layout as the ready-to-install skill ZIP.

## Project layout

```text
research-skills/
  README.md
  CONTRIBUTING.md
  skills/
    aps-quantum-writing/
      SKILL.md
      LICENSE
      references/
      docs/
      assets/
      scripts/
      tests/
```

Each added skill should declare its own name, purpose, version, license, dependencies, and validation scope. Shared catalog changes must not silently change an existing skill's permissions.

## Quality and provenance

The APS skill emphasizes one central scientific question, evidence-linked argument, clear definitions, readable proofs, and informative figures. Its seven-journal metadata index and review-depth limitations are documented in [provenance](skills/aps-quantum-writing/docs/PROVENANCE.md).

Examples are synthetic or explicitly identified demonstrations, not published research results. Tests and format previews do not replace manuscript-specific scientific review.

## Contributions and reports

See [CONTRIBUTING.md](CONTRIBUTING.md). Start with a specific issue and a reproducible example, without uploading private research material. Obtain permission before redistributing modified restricted-license skills.

This repository is independent of APS, OpenAI, and the other projects it cites.
