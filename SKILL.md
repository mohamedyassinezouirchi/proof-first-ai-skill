---
name: proof-first-release-audit
description: Evidence-first release readiness review for software repositories; separate verified checks from assumptions, identify blockers, and make an honest ship/no-ship recommendation.
---

# Proof-First Release Audit

Use this skill when asked to evaluate whether a codebase is ready for a beta, public launch, production release, or customer pilot.

## Principles

1. **Evidence beats confidence.** Never say a check passed unless you actually ran it or received a clearly identified trustworthy test artifact.
2. **No fabricated browsing.** If you cannot access a browser, deployment, credentials, or a third-party service, report that area as **NOT VERIFIED**, not **PASS**.
3. **Do not change production.** Inspections should be read-only by default. Ask for approval before mutating repositories, infrastructure, live user records, auth settings, or billing.
4. **Minimize data exposure.** Never include API keys, credentials, customer records, or private content in reports.
5. **Separate code inspection from user journeys.** Source code existing for a feature does not prove an end-to-end user flow works.
6. **Report reproducibly.** Record command, environment, outcome, and supporting evidence for each verification.

## Procedure

### 1. Define launch scope

Ask or infer from the supplied task:
- Intended launch type (demo, internal alpha, free beta, paid production)
- Supported environments and target users
- Critical user journeys
- Services involved (authentication, database, payment, email)

If unknown, state assumptions explicitly. Do not assume paid checkout must work for a free beta.

### 2. Inventory actual evidence

Review existing documentation, dependency manifests, tests, app routes, environment example files, CI workflows, and deployment setup.

Create an evidence ledger using these statuses:

- **PASS** — Executed verification succeeded with evidence.
- **FAIL** — Executed verification failed with evidence.
- **BLOCKED** — Verification could not proceed due to a specific blocker.
- **NOT VERIFIED** — No sufficiently direct evidence available.
- **NOT APPLICABLE** — Not required for the agreed release scope, with rationale.

An inspection-based finding can be recorded separately, but never upgrade it to a runtime PASS without execution.

### 3. Verify systematically

Where tools and authorization permit, inspect or test:

- Build, typecheck, lint, unit and integration tests
- Authentication and session isolation
- Database ownership/access boundaries
- Critical app flow end-to-end, including mobile
- Localization and accessibility if supported
- Input validation and public endpoints
- Email and password reset if part of scope
- Billing only if paid launch is part of scope
- Observability, backup, rollback, deployment configuration

Never probe a third-party production system or access real customer data without authorization. Favor isolated staging and synthetic fixtures.

### 4. Prioritize gaps

Assign severity:
- **P0** — Security, confidentiality, financial, or data-integrity issue that blocks launch.
- **P1** — Critical user journey broken or unverified; blocks relevant launch.
- **P2** — Important but noncritical limitation.
- **P3** — Polish or future improvement.

Explain the impact and most direct next action.

### 5. Make a scope-specific decision

Output one of:
- **READY** — All critical conditions for the stated launch scope have direct evidence.
- **CONDITIONAL** — Noncritical gaps remain, with explicit conditions and owner.
- **BLOCKED** — A launch-blocking failure or critical unknown remains.

Never infer success from the absence of tests. State evidence freshness.

## Output

Follow [references/report-template.md](references/report-template.md). Include an evidence ledger, critical journey matrix, blockers, and the final decision.

## Stop conditions

Stop and ask for permission before touching production data, changing payment configuration, sending emails, deploying, or publishing private source. If access is denied, produce an honest partial report labeled **NOT VERIFIED**.
