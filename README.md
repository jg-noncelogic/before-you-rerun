# Before you rerun the job

A 10-minute evidence inventory for solo operators and small teams using scheduled or AI-written automations.

A job says **failed**. The tempting response is **Run again**. But a failure message does not tell you whether the job already sent the email, created the row, queued the task, or replaced good data.

In ten minutes, this lesson helps you produce a **preliminary disposition**: what to pause, what evidence to preserve, what destination to check, and whether a rerun is currently allowed. Getting the evidence may take longer.

Use [the one-page card](decision-card.md). Use fictional labels. Never paste tokens, customer data, message bodies, account numbers, or complete logs.

## The one rule

> Do not rerun from the word “failed.” Rerun only after evidence bounds both the outside effect and the state the job touched.

A job can report failure after another system accepted its request but before the job saved confirmation. It can also publish a valid-looking but incomplete file. One incident may require several actions in order; these are not mutually exclusive choices.

## Four plain-language terms

- **Outside effect:** something another person or system could observe, such as an email, payment request, new row, replaced file, or queued task.
- **Effect boundary:** the moment that outside action could first happen.
- **Saved confirmation:** a receipt or record that survives a crash. It must describe the exact lifecycle stage you care about. “Accepted” or “queued” does not necessarily mean “delivered,” “settled,” or “completed.”
- **Stable business key:** the same identifying label used for the same intended action on every attempt. A key is protective only when official behavior or a safe test proves its scope, retention period, duplicate behavior, and response to different payloads under the same key.

## The safe order

### 1. PAUSE new effects

Stop automatic retries and overlapping workers for this job if you can do so within your authority. Record the intended run with a redacted label such as `job-A / morning-slot`.

Do not start another attempt while the original request, worker, or queued task could still complete. A destination lookup followed by a retry has a race: the first attempt might finish after the lookup.

### 2. PRESERVE evidence and state

Before changing anything:

- keep the failed-run identifier and timestamps;
- quarantine suspect output rather than overwriting it;
- preserve the last known good copy;
- avoid “cleanup” that deletes the only evidence of what happened.

Preservation is not restoration. Do not replace live state until you have verified the restore source, checked that it is complete, and ruled out overwriting newer valid state. Prefer validating a copy away from the live path.

### 3. RECONCILE the outside effect

Name one possible outside effect and the system that owns evidence for it. Use a stable redacted lookup key.

The evidence must match the exact stage you are deciding. A provider event that proves “request accepted” does not prove “message delivered.” Absence from an incomplete local log does not prove nothing happened.

Reconciliation can end five ways:

| Finding | Immediate disposition |
|---|---|
| Complete | Close the intended action as completed; **do not rerun** |
| Absent, and the original attempt can no longer complete | Continue to state validation before considering a rerun |
| Pending | Wait with a bounded review time; **do not rerun** |
| Partial or conflicting | Keep paused and follow the owning system’s recovery procedure |
| Unknown | **STOP** until the evidence gap is resolved |

### 4. VALIDATE or RESTORE state

Ask whether local or published state is complete, current, and internally consistent, not merely parseable.

- If state is trustworthy, record the evidence.
- If suspect output exists, keep it quarantined for diagnosis.
- If a restore is needed, validate the restore point away from live state first and confirm it will not erase newer valid work.
- If no trustworthy restore point exists, **STOP** and name the required owner or evidence.

### 5. RERUN only after both risks are bounded

A rerun is allowed only when all of these are true:

1. The prior outside effect is known absent, or verified destination behavior makes repeating the same stable key harmless.
2. The original attempt and any queued or alternate path can no longer create the effect unexpectedly.
3. State is trustworthy or a safe restoration has completed.
4. The rerun uses the same intended business identity and has an observable terminal record.

A new random request ID on every attempt is not duplicate protection. A destination lookup by itself is not duplicate protection. If any condition is unknown, the disposition is **STOP**.

## Try this before reading the answer

A calendar-invite job reports a timeout. The local log has no success line. The calendar already contains an event named `demo-review`, but you cannot tell whether it came from this run. The script creates a new request ID every time. A local attendee cache contains only 3 of the expected 8 fictional people.

On the card, record:

1. the possible outside effect;
2. the evidence owner and exact lifecycle stage;
3. every duplicate/state condition that applies;
4. the immediate action order;
5. whether a rerun is currently allowed.

<details>
<summary>Show the worked resolution</summary>

```text
Job / intended run: calendar-job / demo-review
Possible outside effect: one demo-review invitation was created and may notify attendees
Evidence owner and lookup: calendar / stable event identity and provider event state
Outside-effect status: conflicting; an event exists but is not tied to this run
State status: suspect; attendee cache has 3 of 8 fictional entries
Immediate order: PAUSE -> PRESERVE -> RECONCILE -> VALIDATE
Rerun allowed now: NO, because the existing event, active-request status, duplicate behavior, and complete attendee set are not yet established
```

First pause retries and preserve the event metadata, run timestamps, cache, and last known good data. Reconcile the existing event at the calendar system. If it is complete, close the action and do not rerun. If it is pending, wait. If it is absent, also prove the first request can no longer complete. Quarantine the partial cache and validate a complete source before any later attempt. A new random request ID does not make the rerun safe.

</details>

## Two shorter examples

### Validation stopped before upload

A run-correlated trace from the only worker proves input validation rejected fictional row 8 before any upload or queue call. The worker is terminal, no alternate path exists, and destination state is unchanged. Preserve the trace, correct the fictional fixture, validate state, then **RERUN**. An incomplete debug log would not be enough.

### Report saved 37 of 80 pages

The candidate file parses, but its manifest records only 37 of 80 expected pages. The last known good snapshot still exists. **PAUSE**, preserve both copies, and validate the old snapshot away from the live path. Keep or safely restore verified good state. Do not promote or rerun merely because the candidate parses.

## Your recovery record

```text
Job / intended run: <job-A / morning-slot>
Possible outside effect: <one observable effect>
Evidence owner, key, and lifecycle stage: <system / redacted key / accepted-delivered-completed>
Outside-effect status: <complete / absent / pending / partial / conflicting / unknown>
State status: <trustworthy / suspect / restored-and-verified / unknown>
Immediate order: <PAUSE / PRESERVE / RECONCILE / VALIDATE-RESTORE / STOP>
Rerun allowed now: <YES / NO> because <one evidence sentence>
```

A complete preliminary disposition names the effect, evidence owner, effect stage, state status, immediate sequence, and rerun gate.

## Limits

This lesson does not authorize access, restoration, or a retry. For payment, health, legal, identity, or safety-critical effects, use the responsible human and the owning system’s documented recovery procedure. Vendor idempotency and restore behavior must be verified in official documentation and a safe test environment.

## Go deeper

- [Webhook replay ambiguity](https://github.com/jg-noncelogic/webhook-crash-recovery-drill)
- [Partial snapshot promotion](https://github.com/jg-noncelogic/safe-snapshot-promotion)
- [Crash-safe JSON state](https://github.com/jg-noncelogic/crash-safe-json-state)
- [SQLite restore proof](https://github.com/jg-noncelogic/sqlite-restore-drill)
- [Scheduled automation receipts](https://github.com/jg-noncelogic/reliable-scheduled-automation)

These drills support the synthesis. They do not prove that this lesson benefits a human reader; reader completion and applied decisions remain unobserved.
