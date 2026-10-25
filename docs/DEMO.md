# Demo: Evidence-first release reviews

A short, reproducible way to show what this repository currently does.

## Walkthrough

Open `SKILL.md` and `examples/example-report.md`. Give the skill to a compatible agent with access to a test repository and ask for a free-beta release audit. Compare its report to the included evidence template.

## Suggested content for a public demo

- Show your terminal with the command and actual output.
- Explain the developer problem in one sentence.
- Share the repository link and the specific limitation below.
- Invite practical feedback or a reproducible issue instead of asking for stars.

## Honest limitations

The skill itself cannot execute tests; host-agent tools and authorization determine what can be verified.

## Validation

Run the project's tests where applicable:

```bash
python -m unittest discover -s tests -v
```

Avoid presenting a demo output as a real performance measurement unless you actually collected it.
