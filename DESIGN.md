
# Architecture Decision Records

## ADR-001: Use PDF for Incident Reports

**Status**: Accepted

**Context**
Incident reports are read by auditors and managers, often outside this tool.
They need a fixed format that looks the same wherever it is opened.

**Decision**
Export reports as timestamped PDF files.

**Consequences**
Fixed layout, easy to share and file as audit material.
PDF alone does not prevent or detect tampering: a PDF can still be edited after export.
Tamper detection (recording a hash in a separate, protected store and verifying it later)
is out of scope for this PoC and is a candidate for future work.
Harder to parse programmatically than CSV.

---

## ADR-002: Isolate Secrets in .env

**Status**: Accepted

**Context**
Hardcoded or manually-set API keys are easy to leak,
especially through version control.

**Decision**
Store the key in `.env`, excluded from Git.

**Consequences**
Keeps secrets out of the repository and source code.
Requires local setup per environment.

---

## ADR-003: Treat Log Data as Data, Not Instructions

**Status**: Accepted

**Context**
Log content sent to the model may contain injected instructions.
Relying on the model to resist them is luck, not design.

**Decision**
Wrap log data in tags and instruct the model to treat it strictly as data.

**Consequences**
Adds a layer independent of model behavior.
Not a complete defense, but reduces injection risk.

---

## ADR-004: Validate Input in Stages

**Status**: Accepted

**Context**
Real-world data breaks: missing files, empty CSV, missing columns.
Working only on clean input is not production-ready.

**Decision**
Validate in stages before use: file exists → readable → required columns.

**Consequences**
More upfront code, but fails safely instead of crashing.

---

## ADR-005: Handle API Errors by Type

**Status**: Accepted

**Context**
A single catch-all buries the actual cause,
making operational diagnosis hard.

**Decision**
Handle errors by type: authentication / rate limit / connection.

**Consequences**
More branches, but each failure is traceable in operation.

---

## ADR-006: Cache Analysis Results

**Status**: Accepted

**Context**
Re-calling the API on every UI interaction costs ~25s each time,
even when the input is unchanged.

**Decision**
Cache results; re-run only when input changes.

**Consequences**
Responsive under normal use.
Slightly stale in edge cases where freshness matters.
