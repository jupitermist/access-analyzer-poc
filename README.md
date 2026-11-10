# Access Log Analyzer

Detects access log anomalies with Claude, and exports audit-ready PDF reports.

## Security & Robustness

- API key isolated via `.env` (excluded from Git)
- Input validation: missing files, empty/broken CSV, missing columns
- Prompt injection mitigation: log data is tag-wrapped and treated as data
- Typed API error handling (auth / rate limit / connection)

## Overview

Analyzes access logs (CSV) with Claude to detect anomalies.
Results are shown in a dashboard and exported as timestamped PDF reports.

## Architecture

This PoC is a single LLM call. The focus is the design of the detection:

- **Each user's own normal, not fixed rules.** The model infers each user's usual pattern and flags departures from it. ([ADR-007](DESIGN.md))
- **Findings show their evidence.** Each one reports the normal pattern, the deviation, and the evidence chain. ([ADR-008](DESIGN.md))
- **The hard cases do not fail.** The test logs include self-restored privileges, permissions left after a transfer, and off-hours access from an external IP. All of them succeed, so failed logins do not reveal them. ([ADR-009](DESIGN.md))
- **Detection rate is not established.** Results depended heavily on the evaluation dataset, and the detection logic could not be evaluated on its own. ([ADR-010](DESIGN.md))

## Performance

- Analysis results cached to avoid redundant API calls

## Tech Stack

- Python + Streamlit (UI)
- Claude API (anomaly detection)
- pandas (data handling)
- fpdf2 (PDF generation)

## Setup

```
pip install streamlit pandas anthropic fpdf2 python-dotenv
```

Add your key to `.env`:

```
ANTHROPIC_API_KEY=your_key_here
```

Run:

```
streamlit run app.py
```
