
# Architecture Decision Records

## Detection

### ADR-007: Detect Deviation From Each User's Own Pattern

**Status**: Accepted

**Context**
An action that is routine for one user can be suspicious for another.
What counts as normal differs by user: working hours, source IP, store,
resources accessed, and operations performed.

**Decision**
Have the model infer each user's usual pattern from the logs and flag departures from it,
instead of applying fixed rules to every user.

**Consequences**
The same event can be judged differently for different users.
Requires enough history per user; a new user has no pattern to compare against.
The pattern is inferred by the model, so results may vary between runs.

---

### ADR-008: Require Evidence for Each Finding

**Status**: Accepted

**Context**
A flag alone cannot be acted on. A person has to decide whether a finding is real,
and that requires seeing why the model raised it.

**Decision**
Each finding must report the user's normal pattern, the deviation, and the evidence chain.

**Consequences**
Findings can be reviewed without re-reading the raw logs first.
Output is longer and costs more tokens.
The evidence is not automatically verified against the logs, so a person must confirm it before acting.

---

## Evaluation

### ADR-009: Test With Misuse That Does Not Fail

**Status**: Accepted

**Context**
Misuse by someone with valid access often succeeds at every step.
A detector that relies on failed logins or errors would miss it.

**Decision**
Include test cases where every action succeeds: self-restored privileges,
permissions left after a transfer, and off-hours access from an external IP
with a permission change. Add failed logins by former staff as a decoy.

**Consequences**
Shows whether detection depends on failure signals.
Only three patterns are tested, so this does not show broad coverage.
The patterns were known when the prompt was written, so results may favor them.

---

### ADR-010: Stop Expanding Detection Before It Can Be Measured

**Status**: Accepted

**Context**
Detection results depended heavily on how the evaluation dataset was designed.
Its influence could not be separated from the detection logic,
so the logic could not be evaluated on its own.

**Decision**
Stop expanding the detection logic. Treat evaluation dataset design as a separate challenge.

**Consequences**
No detection rate is reported.
How well it detects beyond the three test patterns is unknown.
The remaining work went to operations (ADR-001 to ADR-006).

---

## Operations

### ADR-001: Use PDF for Incident Reports

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

### ADR-002: Isolate Secrets in .env

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

### ADR-003: Treat Log Data as Data, Not Instructions

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

### ADR-004: Validate Input in Stages

**Status**: Accepted

**Context**
Real-world data breaks: missing files, empty CSV, missing columns.
Working only on clean input is not production-ready.

**Decision**
Validate in stages before use: file exists → readable → required columns.

**Consequences**
More upfront code, but fails safely instead of crashing.

---

### ADR-005: Handle API Errors by Type

**Status**: Accepted

**Context**
A single catch-all buries the actual cause,
making operational diagnosis hard.

**Decision**
Handle errors by type: authentication / rate limit / connection.

**Consequences**
More branches, but each failure is traceable in operation.

---

### ADR-006: Cache Analysis Results

**Status**: Accepted

**Context**
Re-calling the API on every UI interaction costs ~25s each time,
even when the input is unchanged.

**Decision**
Cache results; re-run only when input changes.

**Consequences**
Responsive under normal use.
Slightly stale in edge cases where freshness matters.
