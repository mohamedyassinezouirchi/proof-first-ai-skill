# Proof-First AI Skill

**Stop calling software “launch-ready” without evidence.**

[![Skill structure tests](https://github.com/mohamedyassinezouirchi/proof-first-ai-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/mohamedyassinezouirchi/proof-first-ai-skill/actions/workflows/ci.yml)
![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-84cc16)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An **evidence-first release readiness skill** for AI coding assistants. It teaches an agent to compare launch claims against actual test results, separate verified user journeys from untested functionality, and produce an honest **READY / CONDITIONAL / BLOCKED** decision.

This is a portable **Markdown skill**, not a standalone software tester. It **cannot** run tests, access your repository, use a browser, or inspect deployments unless the host agent independently has those tools and permissions.

## The problem

A production build can pass while sign-up is broken. A route can exist while an end-to-end flow fails. A payment page can render while real billing is not configured.

An AI assistant should not translate “the code looks plausible” into “production ready.”

**Proof-First** asks: *What exactly was tested, where, when, and what is still unverified?*

## What the skill provides

- Evidence-led checks and explicit verification status.
- Critical user-journey inventory.
- Prioritized release blockers and known limitations.
- Honest treatment of inaccessible systems.
- Scope-specific launch decisions.
- A reusable [report template](references/report-template.md).
- An [illustrative sample report](examples/example-report.md) clearly marked as synthetic.

## Verification statuses

| Status | Meaning |
| --- | --- |
| **PASS** | Direct verification succeeded with supporting evidence |
| **FAIL** | Direct verification failed |
| **BLOCKED** | Verification could not run because of a specific blocker |
| **NOT VERIFIED** | Insufficient direct evidence |
| **NOT APPLICABLE** | Explicitly out of scope, with a reason |

**A missing test is never a PASS.**

## Installation

### Compatible agents that support local Markdown skills

Place this repository (or its `SKILL.md`, plus the referenced files) in the host tool's documented skills directory. Location and discovery syntax depend on the host. Check that platform's instructions before installation.

```bash
git clone https://github.com/mohamedyassinezouirchi/proof-first-ai-skill.git
```

This repository uses the common `SKILL.md` format with YAML frontmatter. **Compatibility is not guaranteed across every agent platform**; some tools require additional configuration or a different skill layout.

### No native skill support?

Copy the contents of [SKILL.md](SKILL.md) into an agent's instructions, then supply the [report template](references/report-template.md) as reference context.

## Example invocation

> Review this repository for a **free public beta**. Verify the build, tests, authentication, critical user journeys, and deployment assumptions where tools allow. Use Proof-First statuses and report what you could not verify. Do not deploy or modify production without approval.

An agent without access to a real browser or test environment must mark the corresponding user journeys **NOT VERIFIED** or **BLOCKED**, not falsely claim that they passed.

## Output format

1. Target launch scope and assumptions
2. Executive summary
3. Evidence ledger
4. Critical user journey matrix
5. Prioritized blockers (P0–P3)
6. READY / CONDITIONAL / BLOCKED decision
7. Release conditions and next actions

See [references/report-template.md](references/report-template.md) for a reusable Markdown skeleton.

## Files

```text
proof-first-ai-skill/
├── SKILL.md
├── references/
│   └── report-template.md
├── examples/
│   └── example-report.md
├── tests/
│   └── test_skill_structure.py
├── .github/workflows/
│   └── ci.yml
├── .gitignore
├── LICENSE
└── README.md
```

## Run validation

```bash
python -m unittest discover -s tests -v
```

The current tests validate **file structure and presence of key instructions**, not the real-world quality of arbitrary AI-generated audits. GitHub Actions runs them on push and pull request.

## Safety & limits

- Inspect repositories and staging environments only with authorization.
- Do not access real customer data to “prove” a feature works.
- Do not publish secrets in audit reports.
- Ask before production changes, sending emails, or deploying.
- Reports are advisory and need human review before important launches.
- No claim is made that this is the world's first or only evidence-based audit skill.

## Contributing

Contributions improving checklists, report clarity, compatibility examples, or validation are welcome. Please include reproducible, sanitized examples.

## Author

**Mohamed Yassine Zouirchi** · [GitHub](https://github.com/mohamedyassinezouirchi)

## License

MIT — see [LICENSE](LICENSE).
