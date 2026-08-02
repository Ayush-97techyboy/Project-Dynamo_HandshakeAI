# Project Dynamo - Log Report (`dynamo/log-report`)

A benchmark task environment for **Project Dynamo / Handshake AI**, configured for automated coding agents to extract data and generate verified JSON reports.

---

## 📌 Project Overview

This repository contains a Harbor evaluation task designed to assess AI agents on data extraction and structured reporting.

- **Task Name:** `dynamo/log-report`
- **Category:** Coding / Data Extraction
- **Target Artifact:** `/app/report.json`

---

## 📂 Repository Structure

```text
.
├── instruction.md         # Task prompt given to the AI agent
├── task.toml              # Task metadata, timeout, resource limits, and artifact rules
├── environment/
│   └── Dockerfile         # Base container configuration (Python 3.13-slim & pytest)
├── solution/
│   └── solve.sh           # Reference solution script generating /app/report.json
└── tests/
    ├── test_outputs.py    # Pytest assertions verifying /app/report.json format & values
    └── test.sh            # Verification script executing pytest and writing reward scores
```

---

## ⚙️ Solution & Verification

### Expected Output
The agent must generate `/app/report.json` containing:
```json
{
  "status": "success"
}
```

### Running the Solution
```bash
bash solution/solve.sh
```

### Running the Verifier
```bash
bash tests/test.sh
```
*Outputs verification results and logs to `/logs/verifier/`.*
