# Evidence-first release readiness report

**Repository / application:**  
**Target release:**  
**Date and environment:**  
**Reviewer / tools available:**  
**Overall decision:** READY | CONDITIONAL | BLOCKED

## 1. Executive overview
Two to five sentences, separating implemented features from *verified working* user journeys.

## 2. Evidence ledger

| ID | Area / claim | Status | Evidence (command, test, observation) | Environment / timestamp | Next action |
| --- | --- | --- | --- | --- | --- |
| E-01 | Production build | NOT VERIFIED | No build log available | — | Run build |

Valid statuses: PASS, FAIL, BLOCKED, NOT VERIFIED, NOT APPLICABLE.

## 3. Critical user journeys

| Journey | Status | Supporting evidence / blocker | Owner |
| --- | --- | --- | --- |
| New account signs up and signs in | NOT VERIFIED | Browser access unavailable | — |

## 4. Prioritized gaps

| Priority | Issue / risk | Why it matters | Suggested verification or fix |
| --- | --- | --- | --- |
| P1 | Critical workflow not exercised | Cannot confidently launch beta | Test with synthetic account in staging |

## 5. Release decision

**Decision:**  
**Scope:**  
**Reasoning:**  
**Explicit launch conditions:**  
**Residual risks:**  
**What was not verified:**  

Do not label a release READY unless all critical journeys and safety requirements for the intended scope are supported by direct evidence.
