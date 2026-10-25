# Illustrative report — example only

> This document is a **synthetic example**, not a review of any real repository.

**Repository / application:** sample-agreements-app  
**Target release:** Free public beta  
**Date and environment:** Example staging environment  
**Overall decision:** BLOCKED

| ID | Area / claim | Status | Evidence | Next action |
| --- | --- | --- | --- | --- |
| E-01 | Unit tests | PASS | Hypothetical CI run: 18 tests passed | Keep CI required |
| E-02 | Account sign-up | NOT VERIFIED | No browser session or test account available | Run staging signup test |
| E-03 | Agreement share link | NOT VERIFIED | Endpoint exists in hypothetical code; no end-to-end test | Run with two test identities |
| E-04 | Billing | NOT APPLICABLE | Free beta has no checkout | Revisit before paid launch |

## Critical risk

**P1: Sign-up and core share-link journey are unverified.** A working build alone is not evidence that users can complete the product's main task.

## Decision

**BLOCKED for free public beta** pending direct tests of authentication, agreement creation, and public review. No production or customer data should be altered to obtain that evidence.
