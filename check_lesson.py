#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parent
readme = (root / "README.md").read_text()
card = (root / "decision-card.md").read_text()

checks = {
    "ordered actions in lesson": all(x in readme for x in ("PAUSE", "PRESERVE", "RECONCILE", "VALIDATE", "RERUN", "STOP")),
    "ordered actions in card": all(x in card for x in ("PAUSE", "PRESERVE", "RECONCILE", "VALIDATE/RESTORE", "RERUN", "STOP")),
    "race warning": "first attempt might finish after the lookup" in readme,
    "reconciliation outcomes": all(x in readme for x in ("Complete", "Absent", "Pending", "Partial or conflicting", "Unknown")),
    "effect-stage qualification": "Accepted" in readme and "delivered" in readme and "completed" in readme,
    "idempotency limitations": all(x in readme for x in ("scope", "retention period", "different payloads")),
    "restore preconditions": all(x in readme for x in ("verified the restore source", "overwriting newer valid state", "away from the live path")),
    "cold exercise": "Try this before reading the answer" in readme and "Show the worked resolution" in readme,
    "sensitive-data prohibition in lesson": all(x in readme for x in ("tokens", "customer data", "complete logs")),
    "sensitive-data prohibition in card": all(x in card for x in ("credentials", "customer data", "full logs")),
    "high-stakes boundary in both": "payment, health, legal, identity, or safety-critical" in readme and "payment, health, legal, identity, or safety-critical" in card,
    "compact card": len(card.splitlines()) <= 70,
}

failed = [name for name, ok in checks.items() if not ok]
if failed:
    for name in failed:
        print(f"FAIL: {name}", file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: {len(checks)} structural safety checks")
