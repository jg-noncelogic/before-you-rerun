# Before you rerun: one-page evidence card

Goal: produce a preliminary disposition. Use fictional or redacted labels only.

## 1. PAUSE and PRESERVE

- [ ] Automatic retries, overlapping workers, and queued attempts are paused or accounted for.
- [ ] I preserved run IDs/times, suspect output, and the last known good copy without deleting evidence.

Do not rerun while the original attempt could still complete.

## 2. Name the outside effect

What could another person or system already have observed?

`____________________________________________________________`

If you cannot name it: **STOP**.

## 3. Name the evidence owner

Which destination or provider can prove that exact effect and lifecycle stage? What stable redacted key identifies it?

`Owner: __________ Key: __________ Stage: ____________________`

“Accepted” or “queued” may not mean “delivered” or “completed.” A local exception or missing success line does not prove nothing happened.

## 4. Check all that apply

Outside effect:

- [ ] Complete: close it; do not rerun.
- [ ] Absent, and the original attempt can no longer complete.
- [ ] Pending: wait to a bounded review time; do not rerun.
- [ ] Partial, conflicting, or unknown: **STOP** and reconcile.

Repeat safety:

- [ ] Official behavior or a safe test proves the same stable key cannot create a second effect, including key scope, retention, and changed-payload behavior.
- [ ] A new random key is created each attempt, or behavior is unknown: this is **not** duplicate protection.

State:

- [ ] Trustworthy and complete, with evidence.
- [ ] Suspect or unknown: quarantine it, preserve known-good state, and validate a copy away from the live path.
- [ ] Restore point verified complete and confirmed not to erase newer valid state.

## 5. Record the immediate order

Use as many as apply:

`PAUSE -> PRESERVE -> RECONCILE -> VALIDATE/RESTORE -> STOP/RERUN`

`My order: __________________________________________________`

## 6. Gate the rerun

Rerun only if the prior effect is absent or repetition is proven harmless, the first attempt cannot still complete, and state is trustworthy or safely restored.

`Rerun allowed now: YES / NO because _________________________`

## Safety stop

Do not paste credentials, customer data, message bodies, account numbers, or full logs. For payment, health, legal, identity, or safety-critical effects, use the responsible human and the owning system’s documented recovery procedure.
