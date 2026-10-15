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

A single LLM call, treated as an untrusted component: everything around it is designed
to keep it safe to operate. Each decision is recorded in [DESIGN.md](DESIGN.md).

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
